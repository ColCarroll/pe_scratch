def efficient_exponent(num, power, digits=8):
    modulus = 10 ** digits
    pow_dict = {1: num}
    max_power = 1
    while 2 * max_power < power:
        pow_dict[2 * max_power] = pow_dict[max_power] * pow_dict[max_power] % modulus
        max_power *= 2

    bin_rep = list(bin(power))[-1::-1]

    tot = 1
    for include, (_, value) in zip(bin_rep, sorted(pow_dict.items(), key=lambda j: j[0])):
        if int(include):
            tot = (tot * value) % modulus
    return tot


def tetration(x, n, digits=8):
    modulus = 4 * (10 ** (digits - 1))
    num = x
    for _ in range(n - 1):
        num = efficient_exponent(x, num % modulus, digits=digits)
    return num


def main():
    print(tetration(1777, 1855, 8))


if __name__ == '__main__':
    main()