def fib_gen():
    a = b = 1
    while True:
        yield a
        a, b = a + b, a


def sum_of_even_fib(until):
    fib = fib_gen()
    fib_val = 0
    tot = 0
    while fib_val <= until:
        if fib_val % 2 == 0:
            tot += fib_val
        fib_val = next(fib)
    return tot


def main():
    return sum_of_even_fib(4000000)
