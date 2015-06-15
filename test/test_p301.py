from nose.tools import assert_equal, assert_list_equal
from problems.p301 import bin_vec, nim_sum, nim_add, bin_to_dec, fib_gen, solve_power_of_two, solve


def test_bin_to_dec():
    assert_equal(bin_to_dec([1]), 1)
    assert_equal(bin_to_dec([1, 0]), 2)
    assert_equal(bin_to_dec([1, 1]), 3)
    assert_equal(bin_to_dec([1, 0, 1]), 5)


def test_bin_vec():
    assert_list_equal(bin_vec(1), [1])
    assert_list_equal(bin_vec(2), [1, 0])
    assert_list_equal(bin_vec(3), [1, 1])


def test_nim_add():
    assert_equal(nim_add(2, 1), 3)
    assert_equal(nim_add(3, 4), 7)


def test_nim_sum():
    assert_equal(nim_sum(1, 2, 3), 0)
    assert_equal(nim_sum(1, 2, 2), 1)
    assert_equal(nim_sum(3, 1, 2), 0)


def test_fib_gen():
    fibs = [1, 1, 2, 3, 5, 8, 13]
    fib = fib_gen()
    for elt in fibs:
        assert_equal(elt, next(fib))


def test_solve_power_of_two():
    for j in range(6):
        assert_equal(solve(2**0, 2**6), solve_power_of_two(6))
