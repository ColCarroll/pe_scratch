import math
from utilities.primes import primes


def log_roof(num):
    return 10 ** (int(math.log10(num)) + 1)


def connection(p1, p2):
    mod = log_roof(p1)
    precalc = min(mod, 10000)
    num = p2 + get_rot(p2, p1, precalc) * p2
    p2 *= precalc
    while num % mod != p1:
        num += p2
    return num


def get_rot(p1, p2, mod=10):
    p1 %= mod
    p2 %= mod
    num = p1
    for j in range(mod / 2):
        if num == p2:
            return 2 * j
        num = (num + 2 * p1) % mod
    return None


def solve(upper_bound):
    tot = 0
    prime_list = primes(int(1.01 * upper_bound))
    for idx, prime in (j for j in enumerate(prime_list) if 5 <= j[1] <= upper_bound):
        tot += connection(*prime_list[idx:idx + 2])
    print(tot)


def main():
    return solve(1000000)
