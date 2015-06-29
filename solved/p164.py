"""How many 20 digit numbers n (without any leading zero) exist such that no three consecutive
digits of n have a sum greater than 9?"""


def is_ok(num, max_sum):
    num_str = str(num)
    for j in range(len(num_str)):
        if sum(map(int, list(num_str[j:j + 3]))) > max_sum:
            return False
    return True


def small_sum_digits(start, stop, max_size=9):
    return [j for j in range(start, stop) if is_ok(j, max_size)]


def tail_head(first, second):
    return first[-2:] == second[:-1]


def map_int(num):
    return "{:03d}".format(num)


def consecutive_digit_sum(num_digits, max_sum):
    counter = {map_int(j): 0 for j in small_sum_digits(0, 10 ** 3, max_sum)}
    for key in counter.iterkeys():
        if int(key[0]) > 0:
            counter[key] = 1
    keys = counter.keys()
    sub_counter = {key: 0 for key in counter.iterkeys()}

    for j in range(num_digits - 3):
        for key in counter.iterkeys():
            for second_key in keys:
                if tail_head(second_key, key):
                    sub_counter[key] += counter[second_key]
        counter = dict(sub_counter.items()[:])
        sub_counter = {key: 0 for key in counter.iterkeys()}

    return sum(counter.values())


def main():
    return consecutive_digit_sum(20, 9)

if __name__ == '__main__':
    main()
