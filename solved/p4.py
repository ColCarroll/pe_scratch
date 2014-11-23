def is_palindrome(n):
    n_str = str(n)
    return n_str[-1::-1] == n_str


def largest_palindrome_product(lower, upper):
    #return max(j * k for j in range(lower, upper + 1) for k in range(j, upper + 1) if is_palindrome(j * k))
    max_palindrome = 0
    for j in range(lower, upper + 1):
        for k in range(j, upper + 1):
            if j * k > max_palindrome and is_palindrome(j * k):
                max_palindrome = j * k
    return max_palindrome


def main():
    return largest_palindrome_product(100, 999)
