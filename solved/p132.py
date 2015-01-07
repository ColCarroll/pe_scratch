def f(zeros, reps):
    return int(''.join(str(10 ** zeros) for _ in xrange(reps)) + '1')


def f_iter(zeros, reps):
    yield 1
    for rep in xrange(reps):
        for zero in xrange(zeros):
            yield 0
        yield 1


def factor_repunit(n):
    test = 3
    while len(str(test * test)) <= n:
        if pow(10, n, 9 * test) == 1:
            if is_prime(test):
                yield test
        test += 2


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % j for j in range(3, int(n ** 0.5) + 1, 2))


def main():
    tot = 0
    count = 0
    for j in factor_repunit(10 ** 9):
        count += 1
        tot += j
        if count == 40:
            break
    return tot


if __name__ == '__main__':
    main()
