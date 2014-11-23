def difference(n):  # using python
    return sum(j for j in xrange(1, n + 1)) ** 2 - sum(j ** 2 for j in xrange(1, n + 1))


def difference2(n):  # using math
    return (3 * n ** 4 + 2 * n ** 3 - 3 * n ** 2 - 2 * n) / 12


def main():
    return difference2(100)
