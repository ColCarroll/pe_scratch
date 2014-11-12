def multiples_of(start, end, *multiples):
    return sum(j for j in xrange(start, end + 1) if any(j % multiple == 0 for multiple in multiples))


def main():
    return multiples_of(1, 999, 3, 5)