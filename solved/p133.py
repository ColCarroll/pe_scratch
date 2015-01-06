from utilities.primes import primes, prime_generator


def repunit_factor(n, p):
    return pow(10, 10 ** n, 9 * p) == 1


def divides_small_repunit(primes_to=100):
    prime_list = primes(primes_to)
    found_set = set()
    same_count = 0
    prime_gen = prime_generator()
    while same_count < 5:  # wait for list to stabilize
        found_set_len = len(found_set)
        j = prime_gen.next()
        for p in prime_list:
            if repunit_factor(j, p):
                found_set.add(p)
        if found_set_len == len(found_set):
            same_count += 1
        else:
            same_count = 0
    return sum(prime_list) - sum(found_set)


def main():
    return divides_small_repunit(100000)


if __name__ == '__main__':
    main()
