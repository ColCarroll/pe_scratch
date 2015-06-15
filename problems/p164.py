def small_sum(digits=3, max_size=9):
    for j in range(10 ** digits, 10 ** (digits + 1)):
        if sum(map(int, list(str(j)))) <= max_size:
            yield j


def digit_generator(seed=0, tot_digits=5, max_size=9):
    size = sum(divmod(seed, 10))
    for x in xrange(max_size - size + 1):
        yield digit_generator((seed * 10 + x) % 100, tot_digits - 1, max_size)


def small_consecutive_digits(tot_digits=4):
    tot = 0
    for j in small_sum():
        for x in digit_generator(j % 100):
            yield j * 10 + x


def main():
    tot = 0
    for j in digit_generator(0, 4, 9):
        tot += 1
    print(tot)


if __name__ == '__main__':
    main()
