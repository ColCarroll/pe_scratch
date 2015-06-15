# -*- coding: utf-8 -*-
"""
Nim is a game played with heaps of stones, where two players take it in turn to
remove any number of stones from any heap until no stones remain.

We'll consider the three-heap normal-play version of Nim, which works as follows:
    - At the start of the game there are three heaps of stones.
    - On his turn the player removes any positive number of stones from any single heap.
    - The first player unable to move (because no stones remain) loses.

    If (n1,n2,n3) indicates a Nim position consisting of heaps of size n1, n2 and
    n3 then there is a simple function X(n1,n2,n3) that you may look up or attempt
    to deduce for yourself that returns:

    zero if, with perfect strategy, the player about to move will eventually lose; or
    non-zero if, with perfect strategy, the player about to move will eventually win.
    For example X(1,2,3) = 0 because, no matter what the current player does, his
    opponent can respond with a move that leaves two heaps of equal size, at which
    point every move by the current player can be mirrored by his opponent until no
    stones remain; so the current player loses. To illustrate:
    - current player moves to (1,2,1)
    - opponent moves to (1,0,1)
    - current player moves to (0,0,1)
    - opponent moves to (0,0,0), and so wins.

    For how many positive integers n <= 2 ** 30 does X(n,2n,3n) = 0?
"""


def bin_vec(x):
    return list(map(int, bin(x)[2:]))


def nim_add(x, y):
    x, y = sorted((x, y))
    x_vec, y_vec = map(bin_vec, (x, y))
    x_vec = [0 for _ in range(len(y_vec) - len(x_vec))] + x_vec
    return bin_to_dec([sum(j) % 2 for j in zip(x_vec, y_vec)])


def bin_to_dec(bin_vec):
    tot = 0
    for idx, j in enumerate(bin_vec[-1::-1]):
        tot += 2 ** idx * j
    return tot


def nim_sum(*summands):
    tot = 0
    for summand in summands:
        tot = nim_add(tot, summand)
    return tot


def fib_gen():
    a, b = 1, 0
    while True:
        yield a
        a, b = a + b, a


def solve(start, stop):
    return sum(int(nim_sum(j, 2 * j, 3 * j) == 0) for j in range(start, stop + 1))


def solve_power_of_two(n):
    fib = fib_gen()
    return sum(next(fib) for _ in range(n)) + 1


def main():
    return solve_power_of_two(30)

if __name__ == '__main__':
    main()
