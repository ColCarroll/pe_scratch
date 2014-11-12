def primes(upper_bound):
    prime_list, sieve = [], [True] * (upper_bound + 1)
    for p in range(2, upper_bound + 1):
        if sieve[p]:
            prime_list.append(p)
            for i in range(p * p, upper_bound + 1, p):
                sieve[i] = False
    return prime_list


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