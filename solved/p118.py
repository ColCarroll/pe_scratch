import time
import cProfile
import itertools
from utilities.primes import is_big_prime

IS_PRIME = is_big_prime(987654321)


def is_prime_set(pandigital_set):
    return all(IS_PRIME(j) for j in sorted(pandigital_set))


def partitions(set_):
    if not set_:
        yield []
        return
    for i in xrange(2 ** len(set_) / 2):
        parts = [set(), set()]
        for item in set_:
            parts[i & 1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]] + b


def prime_perms(set_):
    for perm in itertools.permutations(set_):
        if perm[-1] % 2 and sum(perm) % 3:
            num = int("".join(map(str, perm)))
            if IS_PRIME(num):
                yield num


def num_prime_perms(set_):
    if set_ in ({2}, {3}):
        return 1
    return sum(1 for _ in prime_perms(set_))


def pandigital_primes(set_=set(range(1, 10))):
    tot = 0
    for partition in partitions(set_):
        partition_primes = 1
        for set_ in partition:
            partition_primes *= num_prime_perms(set_)
            if not partition_primes:
                break
        tot += partition_primes
    return tot


def main():
    return pandigital_primes()
