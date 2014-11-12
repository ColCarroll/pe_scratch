import time
import itertools
from utilities.primes import is_big_prime


def repeated_number_generator(num_digits, num_repeats, repeated_digit):
    for base_num in range(10 ** (num_digits - num_repeats)):
        for idxs in itertools.combinations(range(num_digits), num_repeats):
            rep_dig_str = str(repeated_digit)
            num = ["" for _ in range(num_digits)]
            base_num_list = list(str(base_num).zfill(num_digits - num_repeats))
            for j in range(num_digits):
                if j in idxs:
                    num[j] = rep_dig_str
                else:
                    num[j] = base_num_list.pop(0)
            if int(num[-1]) * int(num[0]):
                yield int("".join(num))


def max_repeated(num_digits, repeated_digit):
    is_prime = is_big_prime(10 ** (num_digits + 1))
    for repeats in range(num_digits, 1, -1):
        for num in repeated_number_generator(num_digits, repeats, repeated_digit):
            if is_prime(num):
                return repeats
    return 1


def sum_repeated(num_digits, num_repeats, repeated_digit):
    is_prime = is_big_prime(10 ** (num_digits + 1))
    tot = 0
    for num in repeated_number_generator(num_digits, num_repeats, repeated_digit):
        if is_prime(num):
            tot += num
    return tot


def solve(num_digits):
    tot = 0
    for repeated_digit in range(10):
        tot += sum_repeated(num_digits, max_repeated(num_digits, repeated_digit), repeated_digit)
    return tot


def main():
    return solve(10)
