// Exact table-free search for restricted binary numerators divisible by 3^e.
// Compile: g++ -O3 -std=c++17 FILE.cpp -lgmpxx -lgmp -o digit_split
#include <gmpxx.h>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

static mpz_class power(unsigned base, unsigned exponent) {
    mpz_class result;
    mpz_ui_pow_ui(result.get_mpz_t(), base, exponent);
    return result;
}

static bool check_degree(unsigned n, unsigned exponent, unsigned max_right_bits) {
    if (!n || !exponent) throw std::invalid_argument("degree and threshold must be positive");
    mpz_class modulus = power(3, exponent);
    std::vector<mpz_class> maxima(1, 0);
    mpz_class two_power = 1;
    unsigned left_count = 0;
    while (left_count < n - 1) {
        mpz_class next = 5 * maxima.back() + two_power;
        if (next >= modulus) break;
        maxima.push_back(next);
        ++left_count;
        two_power *= 2;
    }
    unsigned right_count = n - 1 - left_count;
    if (right_count > max_right_bits || right_count >= 63)
        throw std::runtime_error("inconclusive: right-subset count exceeds cap");

    std::vector<mpz_class> five_powers;
    mpz_class five_power = 1;
    for (unsigned i = 0; i < left_count; ++i) {
        five_powers.push_back(five_power);
        five_power *= 5;
    }
    mpz_class factor = 2 * power(5, n - left_count), inverse;
    if (!mpz_invert(inverse.get_mpz_t(), factor.get_mpz_t(), modulus.get_mpz_t()))
        throw std::logic_error("left block factor must be invertible");
    mpz_class target = (-(power(5, n) + power(2, n)) * inverse) % modulus;
    if (target < 0) target += modulus;
    std::vector<mpz_class> weights;
    for (unsigned i = left_count + 1; i < n; ++i)
        weights.push_back((power(2, i) * power(5, n - i) * inverse) % modulus);

    uint64_t subset_count = uint64_t(1) << right_count;
    uint64_t decoded_candidates = 0, checked = 0, matching_mask = 0;
    std::vector<unsigned> decoded_digits(left_count, 0);
    bool found = false;
    mpz_class current = 0, candidate;
    auto started = std::chrono::steady_clock::now();
    for (uint64_t step = 0; step < subset_count; ++step) {
        uint64_t gray = step ^ (step >> 1);
        if (step) {
            unsigned bit = __builtin_ctzll(step);
            if (gray & (uint64_t(1) << bit)) {
                mpz_add(current.get_mpz_t(), current.get_mpz_t(), weights[bit].get_mpz_t());
                if (mpz_cmp(current.get_mpz_t(), modulus.get_mpz_t()) >= 0)
                    mpz_sub(current.get_mpz_t(), current.get_mpz_t(), modulus.get_mpz_t());
            } else {
                mpz_sub(current.get_mpz_t(), current.get_mpz_t(), weights[bit].get_mpz_t());
                if (mpz_sgn(current.get_mpz_t()) < 0)
                    mpz_add(current.get_mpz_t(), current.get_mpz_t(), modulus.get_mpz_t());
            }
        }
        checked = step + 1;
        mpz_sub(candidate.get_mpz_t(), target.get_mpz_t(), current.get_mpz_t());
        if (mpz_sgn(candidate.get_mpz_t()) < 0)
            mpz_add(candidate.get_mpz_t(), candidate.get_mpz_t(), modulus.get_mpz_t());
        if (mpz_cmp(candidate.get_mpz_t(), maxima.back().get_mpz_t()) > 0) continue;
        ++decoded_candidates;
        unsigned digits = 0;
        for (unsigned j = left_count; j-- > 0;) {
            if (mpz_cmp(candidate.get_mpz_t(), maxima[j + 1].get_mpz_t()) > 0) break;
            unsigned digit = mpz_odd_p(candidate.get_mpz_t()) ? 1 : 0;
            if (digit) {
                mpz_sub(candidate.get_mpz_t(), candidate.get_mpz_t(), five_powers[j].get_mpz_t());
                if (mpz_sgn(candidate.get_mpz_t()) < 0) break;
            }
            mpz_fdiv_q_2exp(candidate.get_mpz_t(), candidate.get_mpz_t(), 1);
            decoded_digits[digits++] = digit;
        }
        if (digits == left_count && mpz_sgn(candidate.get_mpz_t()) == 0) {
            found = true;
            matching_mask = gray;
            break;
        }
    }

    std::cout << "{\"degree\":" << n << ",\"valuation_threshold\":" << exponent
              << ",\"left_digits\":" << left_count << ",\"right_digits\":" << right_count
              << ",\"right_subsets\":" << subset_count << ",\"right_checked\":" << checked
              << ",\"modulus\":\"" << modulus << "\",\"left_maximum\":\"" << maxima.back()
              << "\",\"threshold_match\":" << (found ? "true" : "false");
    if (found) {
        std::vector<unsigned> coefficients(n + 1, 0);
        coefficients.front() = coefficients.back() = 1;
        for (unsigned i = 0; i < left_count; ++i) coefficients[i + 1] = decoded_digits[i];
        for (unsigned i = 0; i < right_count; ++i) coefficients[left_count + i + 1] = (matching_mask >> i) & 1;
        mpz_class numerator = 0;
        for (unsigned i = 0; i <= n; ++i)
            if (coefficients[i]) numerator += power(2, i) * power(5, n - i);
        if (!mpz_divisible_p(numerator.get_mpz_t(), modulus.get_mpz_t()))
            throw std::logic_error("exact witness reconstruction failed");
        mpz_class outside = numerator;
        unsigned valuation = 0;
        while (mpz_divisible_ui_p(outside.get_mpz_t(), 3)) {
            mpz_divexact_ui(outside.get_mpz_t(), outside.get_mpz_t(), 3);
            ++valuation;
        }
        std::cout << ",\"coefficients\":[";
        for (unsigned i = 0; i <= n; ++i) std::cout << (i ? "," : "") << coefficients[i];
        std::cout << "],\"numerator\":\"" << numerator << "\",\"v3\":" << valuation
                  << ",\"outside_part\":\"" << outside << "\",\"violates_degree_bound\":"
                  << (valuation > n ? "true" : "false");
    }
    double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - started).count();
    std::cout << ",\"decoded_candidates\":" << decoded_candidates << ",\"seconds\":" << seconds << "}" << std::endl;
    return found;
}

int main(int argc, char** argv) {
    try {
        if (argc < 3 || argc > 5)
            throw std::invalid_argument("usage: digit_split START STOP [OFFSET=1] [MAX_RIGHT_BITS=30]");
        unsigned start = std::stoul(argv[1]), stop = std::stoul(argv[2]);
        int offset = argc > 3 ? std::stoi(argv[3]) : 1;
        unsigned cap = argc > 4 ? std::stoul(argv[4]) : 30;
        if (offset < -1000 || offset > 1000)
            throw std::invalid_argument("offset must lie between -1000 and 1000");
        if (!start || start > stop || stop > 1000 || int(start) + offset < 1 || cap > 62)
            throw std::invalid_argument("invalid degree range, threshold, or resource cap");
        for (unsigned n = start; n <= stop; ++n)
            if (check_degree(n, unsigned(int(n) + offset), cap)) break;
    } catch (const std::exception& error) {
        std::cerr << error.what() << std::endl;
        return 2;
    }
    return 0;
}
