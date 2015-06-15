"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.
What is the expected number of distinct colors in 20 randomly picked balls?
Give your answer with nine digits after the decimal point (a.bcdefghij).
"""

import operator
import itertools


def prod(iterator):
    return reduce(operator.mul, iterator)


def product(a, b):
    return prod(xrange(a, b + 1))


def factorial(n):
    if n == 1:
        return 1
    if n < 1:
        return 0
    return product(2, n)


def binom(p, q):
    if 0 <= q < p:
        return product(q + 1, p) / product(1, p - q)
    if p == q:
        return 1
    if q > p or q < 0:
        return 0


def partitions(n):
    """Integer partitions of n
    """
    parts = set()
    parts.add((n, ))
    for j in range(1, n):
        for k in partitions(n - j):
            parts.add(tuple((j, ) + k))
    return parts


class ManualUrn(object):
    """ Actually counts all ways of drawing from an urn
    """
    def __init__(self, colors, balls):
        self.colors = colors
        self.balls = balls
        self._urn = [j for _ in range(balls) for j in range(colors)]

    def ways_to_draw_n_or_fewer_colors(self, n, draws):
        tot = 0
        for draw in itertools.combinations(self._urn, draws):
            tot += (len(set(draw)) <= n)
        return tot

    def ways_to_draw_n_colors(self, n, draws):
        tot = 0
        for draw in itertools.combinations(self._urn, draws):
            tot += (len(set(draw)) == n)
        return tot


class Urn(object):
    """Creates an urn with <balls> balls of <colors> colors, so there will be
    a total of <balls> * <colors> balls in the urn.
    """
    def __init__(self, colors, balls):
        self.colors = colors
        self.balls = balls
        self._ways_to_draw = []

    def ways_to_draw_n_or_fewer_colors(self, n, draws):
        return binom(self.balls, n) * binom(self.balls * n, draws)

    def ways_to_draw_n_colors(self, n, draws):
        return binom(self.balls, n) * binom(self.balls * n, draws)
