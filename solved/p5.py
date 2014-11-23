from collections import Counter
from utilities.primes import factor_big_nums


def all_divides(max_val):
    factor = factor_big_nums(max_val)
    all_factors = Counter()
    for j in xrange(2, max_val + 1):
        num_factors = Counter(factor(j))
        for num_factor, count in num_factors.iteritems():
            all_factors[num_factor] = max(all_factors[num_factor], count)
    smallest = 1
    for key, value in all_factors.iteritems():
        smallest *= (key ** value)
    return smallest


def main():
    return all_divides(20)