import unittest
from nose.tools import assert_equal, assert_list_equal
from problems.p493 import prod, product, factorial, binom, partitions, ManualUrn, Urn


def test_prod():
    assert_equal(prod((1, 2, 3)), 1 * 2 * 3)
    assert_equal(prod((-1, 2, 3)), -1 * 2 * 3)


def test_product():
    assert_equal(product(2, 5), 2 * 3 * 4 * 5)


def test_factorial():
    assert_equal(factorial(0), 0)
    assert_equal(factorial(1), 1)
    assert_equal(factorial(2), 2)
    assert_equal(factorial(5), 5 * 4 * 3 * 2 * 1)


def test_binom():
    for j in range(3, 10):
        assert_equal(binom(j, 0), 1)
        assert_equal(binom(j, 1), j)
        assert_equal(binom(j, 2), (j * j - j) / 2)
        assert_equal(binom(j, j - 2), (j * j - j) / 2)
        assert_equal(binom(j, j - 1), j)
        assert_equal(binom(j, j), 1)
        assert_equal(binom(j, j + 1), 0)


def test_partitions():
    assert_list_equal(sorted(partitions(4)),
                      [(1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1), (4,)])


class TestUrn(unittest.TestCase):
    def setUp(self):
        self.colors = 3
        self.balls = 2
        self.urn = ManualUrn(self.colors, self.balls)

    def error_message(self, num_colors, num_balls, draws, colors, true, computed):
        return "In an urn with {} balls of {} colors, there are {} ways to draw {} colors,"\
            " picking {} at a time, not {}".format(
                num_balls, num_colors, true, colors, draws, computed)
