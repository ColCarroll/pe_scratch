from nose.tools import assert_list_equal, assert_equal, assert_true, assert_false
from utilities.primes import prime_generator, primes, nth_prime, solve_monotone_func, is_big_prime, factor_big_nums, factor_num, divisor_gen, divisor_gen_from_factors

small_primes = (2, 3, 5, 7, 11, 13, 17, 19)

def test_prime_generator():
    gen = prime_generator()
    for p in small_primes:
        p == next(gen)

def test_primes():
    assert_list_equal(primes(20), list(small_primes))

def test_nth_prime():
    for j, p in enumerate(small_primes, 1):
        assert_equal(nth_prime(j), p)
    assert_equal(nth_prime(-2), 0)

def test_solve_monotone_function():
    assert_equal(solve_monotone_func(lambda x: x * x, 20 * 20, 0), 20)

def test_is_big_prime():
    p = is_big_prime(1000000)
    for j in range(20):
        if j in small_primes:
            assert_true(p(j))
        else:
            assert_false(p(j))

def test_factor_big_nums():
    big_num = reduce(lambda j, k: j * k, small_primes)
    factor = factor_big_nums(big_num)
    factors = sorted(list(factor(big_num)))
    assert_list_equal(factors, list(small_primes))

def test_factor_nums():
    big_num = reduce(lambda j, k: j * k, small_primes)
    factors = sorted(list(factor_num(big_num)))
    assert_list_equal(factors, list(small_primes))

def test_divisor_gen():
    assert_list_equal(sorted(list(divisor_gen(6))), [1, 2, 3, 6])

def test_divisor_gen_from_factors():
    six_factors = [1, 2, 3, 6]
    assert_list_equal(sorted(list(divisor_gen_from_factors([2, 3]))), six_factors)
    assert_list_equal(sorted(list(divisor_gen_from_factors([3, 2, 1]))), six_factors)
