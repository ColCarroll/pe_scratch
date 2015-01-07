from collections import Counter
import math


def prime_generator():
    prime_nums = [2]
    counter = 3
    yield 2
    while True:
        j = 0
        is_prime = True
        while prime_nums[j] * prime_nums[j] <= counter:
            if counter % prime_nums[j] == 0:
                is_prime = False
                break
            j += 1
        if is_prime:
            prime_nums.append(counter)
            yield prime_nums[-1]
        counter += 2


def primes(upper_bound):
    prime_list, sieve = [2], [True, True] + ([False, True] * (upper_bound / 2))
    for p in xrange(3, upper_bound + 1):
        if sieve[p]:
            prime_list.append(p)
            for i in range(p * p, upper_bound + 1, p):
                sieve[i] = False
    return prime_list


def nth_prime(n):
    """
    :param n: Integer, which prime you want to find
    :return: the nth prime number.  ex: nth_prime(1) returns 2, and nth_prime(4) returns 7
    """
    upper_bound = solve_monotone_func(lambda x: x / math.log(x), n, 2)  # prime number theorem
    sieve = [True, True] + ([False, True] * (upper_bound / 2))
    primes_found = 0
    for p in xrange(2, upper_bound + 1):
        if sieve[p]:
            primes_found += 1
            if primes_found == n:
                return p
            for i in range(p * p, upper_bound + 1, p):
                sieve[i] = False


def solve_monotone_func(func, equals, start=0):
    """
    :param func: A monotonic increasing function of an integer
    :param equals: A number you'd like the function to be equal to
    :param start: Where to start checking.  Usually 0 is good (unless func = x / log(x), or something)
    :return: the natural number n such that abs(func(n) - equals) is minimized
    """
    candidate = start
    sign = 1
    step = 1
    while func(candidate) < equals:
        candidate += sign * step
        step *= 2

    while step > 1:
        step /= 2
        sign = cmp(equals, func(candidate))
        while cmp(equals, func(candidate)) == sign:
            candidate += sign * step

    other_candidate = candidate - sign * step
    if abs(func(other_candidate) - equals) < abs(func(candidate) - equals):
        return other_candidate
    return candidate


def is_big_prime(upper_bound):
    p = primes(int(upper_bound ** 0.5) + 1)

    def is_prime(j):
        if j <= 1:
            return False
        for prime in p:
            if prime * prime > j:
                return True
            if not j % prime:
                return False
        return True

    return is_prime


def factor_big_nums(upper_bound):
    """
    Use to repeatedly factor big numbers
    :param upper_bound: The largest number you'll factor
    :return: A function that returns an iterator over the factors of a large number
    """
    p = primes(int(upper_bound ** 0.5) + 1)

    def factor(num):
        for prime in p:
            while num % prime == 0:
                yield prime
                num /= prime
            if prime * prime > num:
                break
        if num > 1:
            yield num

    return factor


def factor_num(num):
    """
    Use for factoring single numbers
    :param num: number to factor
    :return: iterator over the factors
    """
    while num % 2 == 0:
        yield 2
        num /= 2
    prime = 3
    while prime * prime <= num:
        while num % prime == 0:
            yield prime
            num /= prime
        prime += 2
    if num > 1:
        yield num


def divisor_gen(num):
    factors = Counter(factor_num(num)).items()
    n_factors = len(factors)
    f = [0] * n_factors
    while True:
        yield reduce(lambda x, y: x * y, [factors[x][0] ** f[x] for x in xrange(n_factors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= n_factors:
                return

