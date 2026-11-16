"""Exact {2,3}-smooth critical-orbit scan for N_0[5/6].

The completed finite range is evidence only; the scan does not decide global
atomicity or IDF. Denominator depth means the minimal n with denominator
dividing 6**n. All arithmetic, candidate bounds, and orbit tests are exact.
"""
import argparse
import json
import time


def critical_terminal(numerator, denominator, depth):
    for step in range(depth):
        digit = numerator % 5
        numerator = (numerator - digit * denominator) // 5
        denominator //= 6
        if numerator < 0 or numerator > 24 * denominator:
            return None, step + 1
    return numerator, depth


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--start', type=int, default=1)
    args = parser.parse_args()
    if not 1 <= args.start <= args.limit:
        parser.error('require 1 <= start <= limit')
    start = time.monotonic()
    previous = args.start - 1
    power3n = 3**previous
    denominator6 = 6**previous
    power2n = 2**previous
    if previous:
        low, high = 0, previous
        while low < high:
            middle = (low + high) // 2
            if 3**middle > power2n:
                high = middle
            else:
                low = middle + 1
        exponent3 = low
    else:
        exponent3 = 0
    power3m = 3**exponent3
    numerator3 = 3**(exponent3 + previous)
    total = hits = max_reject_steps = 0
    with open(args.output, 'w') as output:
        output.write(json.dumps({'kind':'metadata','start':args.start,'limit':args.limit,
                                 'interval':'1 < x <= 24','exact':True})+'\n')
        for n in range(args.start, args.limit + 1):
            power3n *= 3
            denominator6 *= 6
            power2n *= 2
            exponent2 = power3n.bit_length()
            numerator2 = 1 << (exponent2 + n)
            while numerator2 <= 24 * denominator6:
                terminal, steps = critical_terminal(numerator2, denominator6, n)
                total += 1
                if terminal is not None:
                    hits += 1
                    row={'kind':'critical','numerator_prime':2,'numerator_exponent':exponent2,
                         'denominator_prime':3,'denominator_exponent':n,'terminal':terminal}
                    output.write(json.dumps(row)+'\n')
                    output.flush()
                    print(json.dumps(row), flush=True)
                else:
                    max_reject_steps = max(max_reject_steps, steps)
                exponent2 += 1
                numerator2 *= 2
            numerator3 *= 3
            while power3m <= power2n:
                power3m *= 3
                numerator3 *= 3
                exponent3 += 1
            candidate3, m = numerator3, exponent3
            while candidate3 <= 24 * denominator6:
                terminal, steps = critical_terminal(candidate3, denominator6, n)
                total += 1
                if terminal is not None:
                    hits += 1
                    row={'kind':'critical','numerator_prime':3,'numerator_exponent':m,
                         'denominator_prime':2,'denominator_exponent':n,'terminal':terminal}
                    output.write(json.dumps(row)+'\n')
                    output.flush()
                    print(json.dumps(row), flush=True)
                else:
                    max_reject_steps = max(max_reject_steps, steps)
                m += 1
                candidate3 *= 3
            if n % 10000 == 0 or n == args.limit:
                report={'kind':'progress','depth':n,'candidates':total,'critical':hits,
                        'max_reject_steps':max_reject_steps,'elapsed_seconds':round(time.monotonic()-start,2)}
                output.write(json.dumps(report)+'\n')
                output.flush()
                print(json.dumps(report),flush=True)
        output.write(json.dumps({'kind':'complete','depth':args.limit,'candidates':total,'critical':hits})+'\n')


if __name__ == '__main__':
    main()
