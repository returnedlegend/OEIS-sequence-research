// Exact subset-sum search for binary f(2/5) with v_3(5^n f(2/5)) >= n+offset.
// No floating-point arithmetic participates in any mathematical decision.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using U = unsigned __int128;

// Only witness reconstruction needs integers larger than 128 bits.
struct Big {
    static constexpr uint64_t base = 1000000000;
    std::vector<uint32_t> words;
    explicit Big(uint32_t value = 0) : words(1, value) {}
    void multiply(unsigned factor) {
        uint64_t carry = 0;
        for (auto& word : words) { uint64_t v = uint64_t(word) * factor + carry; word = v % base; carry = v / base; }
        if (carry) words.push_back(carry);
    }
    void add(const Big& other) {
        words.resize(std::max(words.size(), other.words.size()), 0);
        uint64_t carry = 0;
        for (size_t i = 0; i < words.size(); ++i) {
            uint64_t v = uint64_t(words[i]) + carry + (i < other.words.size() ? other.words[i] : 0);
            words[i] = v % base; carry = v / base;
        }
        if (carry) words.push_back(carry);
    }
    unsigned remainder(unsigned divisor) const {
        uint64_t carry = 0;
        for (size_t i = words.size(); i-- > 0;) carry = (carry * base + words[i]) % divisor;
        return carry;
    }
    void divide(unsigned divisor) {
        uint64_t carry = 0;
        for (size_t i = words.size(); i-- > 0;) { uint64_t v = carry * base + words[i]; words[i] = v / divisor; carry = v % divisor; }
        while (words.size() > 1 && words.back() == 0) words.pop_back();
    }
    std::string str() const {
        std::ostringstream out;
        out << words.back();
        for (size_t i = words.size() - 1; i-- > 0;) out << std::setw(9) << std::setfill('0') << words[i];
        return out.str();
    }
};

static std::string decimal(U x) {
    if (!x) return "0";
    std::string out;
    while (x) { out.push_back(char('0' + x % 10)); x /= 10; }
    std::reverse(out.begin(), out.end());
    return out;
}

static U small_power(unsigned base, unsigned exponent, U modulus) {
    U value = 1 % modulus;
    while (exponent--) value = (value * base) % modulus;
    return value;
}

static U subtract_mod(U a, U b, U modulus) {
    return a >= b ? a - b : modulus - (b - a);
}

// Each Gray step changes exactly the subset bit indexed by ctz(step).
static void next_gray(U& value, uint64_t step, const std::vector<U>& weights, U modulus) {
    unsigned index = __builtin_ctzll(step);
    U weight = weights[index];
    uint64_t gray = step ^ (step >> 1);
    if (gray & (uint64_t(1) << index)) {
        value += weight;
        if (value >= modulus) value -= modulus;
    } else {
        value = subtract_mod(value, weight, modulus);
    }
}

static std::vector<U> sorted_residues(const std::vector<U>& weights, U modulus,
                                     bool complements, U target) {
    uint64_t count = uint64_t(1) << weights.size();
    std::vector<U> result(count);
    U value = 0;
    for (uint64_t step = 0; step < count; ++step) {
        if (step) next_gray(value, step, weights, modulus);
        result[step] = complements ? subtract_mod(target, value, modulus) : value;
    }
    std::sort(result.begin(), result.end());
    return result;
}

static uint64_t recover_mask(const std::vector<U>& weights, U modulus, U wanted) {
    U value = 0;
    uint64_t count = uint64_t(1) << weights.size();
    for (uint64_t step = 0; step < count; ++step) {
        if (step) next_gray(value, step, weights, modulus);
        if (value == wanted) return step ^ (step >> 1);
    }
    throw std::logic_error("matching residue has no subset witness");
}

static bool check_degree(unsigned n, unsigned offset, unsigned max_half_bits) {
    // The following bounds make all setup products <= 5*3^73 < 2^128.
    if (n < 1 || n > 70 || offset > 3)
        throw std::invalid_argument("require 1 <= degree <= 70 and 0 <= offset <= 3");
    unsigned middle = n - 1, left_count = middle / 2, right_count = middle - left_count;
    if (right_count > max_half_bits)
        throw std::runtime_error("inconclusive: half-size cap exceeded");
    U modulus = 1;
    for (unsigned i = 0; i < n + offset; ++i) modulus *= 3;
    std::vector<U> weights;
    for (unsigned i = 1; i < n; ++i) {
        U value = small_power(5, n - i, modulus);
        for (unsigned j = 0; j < i; ++j) value = (2 * value) % modulus;
        weights.push_back(value);
    }
    U endpoint = (small_power(5, n, modulus) + small_power(2, n, modulus)) % modulus;
    U target = endpoint ? modulus - endpoint : 0;
    std::vector<U> left(weights.begin(), weights.begin() + left_count);
    std::vector<U> right(weights.begin() + left_count, weights.end());
    auto start = std::chrono::steady_clock::now();
    auto left_values = sorted_residues(left, modulus, false, target);
    auto right_values = sorted_residues(right, modulus, true, target);
    size_t i = 0, j = 0;
    bool found = false;
    U matching = 0;
    while (i < left_values.size() && j < right_values.size()) {
        if (left_values[i] == right_values[j]) { found = true; matching = left_values[i]; break; }
        if (left_values[i] < right_values[j]) ++i; else ++j;
    }
    std::cout << "{\"degree\":" << n << ",\"valuation_threshold\":" << n + offset
              << ",\"modulus\":\"" << decimal(modulus) << "\",\"left_subsets\":"
              << left_values.size() << ",\"right_subsets\":" << right_values.size()
              << ",\"threshold_match\":" << (found ? "true" : "false");
    if (found) {
        uint64_t lm = recover_mask(left, modulus, matching);
        uint64_t rm = recover_mask(right, modulus, subtract_mod(target, matching, modulus));
        std::vector<unsigned> coefficients(n + 1, 0);
        coefficients.front() = coefficients.back() = 1;
        for (unsigned bit = 0; bit < left_count; ++bit) coefficients[bit + 1] = (lm >> bit) & 1;
        for (unsigned bit = 0; bit < right_count; ++bit) coefficients[left_count + bit + 1] = (rm >> bit) & 1;
        Big numerator;
        for (unsigned bit = 0; bit <= n; ++bit) if (coefficients[bit]) {
            Big term(1);
            for (unsigned power = 0; power < bit; ++power) term.multiply(2);
            for (unsigned power = bit; power < n; ++power) term.multiply(5);
            numerator.add(term);
        }
        Big remaining = numerator;
        unsigned valuation = 0;
        while (remaining.remainder(3) == 0) { remaining.divide(3); ++valuation; }
        if (valuation < n + offset) throw std::logic_error("exact witness verification failed");
        std::cout << ",\"coefficients\":[";
        for (unsigned bit = 0; bit <= n; ++bit) std::cout << (bit ? "," : "") << coefficients[bit];
        std::cout << "],\"numerator\":\"" << numerator.str() << "\",\"v3\":" << valuation
                  << ",\"outside_part\":\"" << remaining.str() << "\",\"violates_degree_bound\":"
                  << (valuation > n ? "true" : "false");
    }
    double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
    std::cout << ",\"seconds\":" << seconds << "}" << std::endl;
    return found;
}

int main(int argc, char** argv) {
    try {
        if (argc < 3 || argc > 5) throw std::invalid_argument("usage: mitm START STOP [OFFSET=1] [MAX_HALF_BITS=28]");
        unsigned start = std::stoul(argv[1]), stop = std::stoul(argv[2]);
        unsigned offset = argc > 3 ? std::stoul(argv[3]) : 1;
        unsigned cap = argc > 4 ? std::stoul(argv[4]) : 28;
        if (start > stop || stop > 70 || cap > 30) throw std::invalid_argument("invalid range or cap");
        for (unsigned n = start; n <= stop; ++n) if (check_degree(n, offset, cap)) break;
    } catch (const std::exception& error) {
        std::cerr << error.what() << std::endl;
        return 2;
    }
}
