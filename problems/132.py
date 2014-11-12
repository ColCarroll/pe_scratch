from utilities.primes import factor_big_nums


def repunit(num_digs):
    return int("".join("1" for _ in range(num_digs)))


def factor(num):
    return factor_big_nums(num)(num)

def factor_repunit(num_digs):
    factor = factor_big_nums(10 ** num_digs)
    return factor(repunit(num_digs) / 11)


def main():
    for num_digs in range(2, 18, 2):
        print(repunit(num_digs) / 11)
        for fac in factor(repunit(num_digs) / 11):
            print fac
        print("\n")


if __name__ == '__main__':
    main()