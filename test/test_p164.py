from nose.tools import assert_equal, assert_true, assert_false
from solved.p164 import small_sum_digits, consecutive_digit_sum, tail_head, is_ok, map_int


def test_is_ok():
    assert_true(is_ok(207, 9))
    assert_false(is_ok(217, 9))
    assert_true(is_ok(5117, 9))


def test_map_int():
    assert_equal(map_int(1), '001')
    assert_equal(map_int(101), '101')


def test_tail_head():
    assert_true(tail_head("123", "236"))
    assert_true(tail_head("101", "012"))
    assert_false(tail_head("122", "211"))
    assert_false(tail_head("100", "012"))
    assert_true(tail_head("100", "001"))
    assert_true(tail_head("110", "100"))
    assert_false(tail_head("100", "012"))
    assert_true(tail_head("202", "020"))


def test_consecutive_digit_sum():
    for digs in range(3, 6):
        max_size = 9
        right_answer = len(small_sum_digits(10 ** (digs - 1), 10 ** digs, max_size))
        compute_answer = consecutive_digit_sum(digs, max_size)
        print(compute_answer, right_answer)
        assert_equal(right_answer, compute_answer,
                     "There are {} numbers with {} digits summing to less than {}, not {}".format(
                         right_answer, digs, max_size, compute_answer))
