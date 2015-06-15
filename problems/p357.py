"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""

from utilities.primes import primes, divisor_gen_from_factors, factor_num
from itertools import combinations
import time

def is_special(n, prime_list):
    if n % 2:
        return False
    factors = []
    factored = n
    for p in prime_list:
        if factored % p == 0:
            factors.append(p)
            factored /= p
            if factored % p == 0: # necessary, but not sufficient that n isn't divisible by p^2
                return False
        if p * p > factored:
            break
    if factored > 0:
        factors.append(factored)
    for divisor in divisor_gen_from_factors(factors):
        if not is_prime(divisor + n / divisor, prime_list):
            return False
    return True


def is_prime(n, prime_list):
    for p in prime_list:
        if n % p == 0:
            return False
        if p * p > n:
            return True
    return True

def special_sum(up_to_n):
    polling_interval = 1000000
    prime_list = [p for p in primes(int((up_to_n + 1) ** 0.5) + 1)]
    tot = 0
    t0 = time.time()
    for j in xrange(2, up_to_n, 4):
        if is_special(j, prime_list):
            print(j)
            tot += j
        if (j - 2) % polling_interval == 0:
            t = time.time() - t0
            t0 = time.time()
            print("[{:.2f}s, {:,.0f}/s] {:,d} out of {:,d}".format(t, polling_interval / t, j - 2, up_to_n))
    return tot

def prod(a_list):
    return reduce(lambda j, k: j * k, a_list, 1)

def gen_special(up_to_n):
    yield 2
    print("generating list...")
    prime_list = primes(up_to_n / 2)
    print("have primes.  finding max number of factors.")
    max_length = next(j for j, _ in enumerate(prime_list) if prod(prime_list[:j]) > up_to_n)
    print("max factors is {:d}.  Analyzing factors.".format(max_length))
    for j in range(1, max_length + 1):
        print("Analyzing factors of length {:d}".format(j))
        for factors in combinations(prime_list[1:], j):
            print(factors)
            n = 2 * prod(factors)
            if n > up_to_n:
                break
            if all(is_prime(divisor + n / divisor, prime_list) for divisor in divisor_gen_from_factors(list(factors) + [2])):
                yield n



def scratch(up_to_n):
    prime_list = [p for p in primes(int((up_to_n + 1) ** 0.5) + 1)]
    t0 = time.time()
    for j in xrange(2, up_to_n, 4):
        if is_special(j, prime_list):
            print(j, list(factor_num(j)))


def main():
    up_to_n = 100
    for j in sorted(gen_special(up_to_n)):
        print(j)
