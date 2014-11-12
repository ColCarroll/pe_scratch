from utilities.primes import factor_num


def largest_factor(num):
    return max(j for j in factor_num(num))


def main():
    return largest_factor(600851475143)
