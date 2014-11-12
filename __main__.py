import sys
import re
import time
from problems import *
from solved import *


def dummy_func(string):
    def func():
        print(string)

    return func


def can_solve():
    args = sys.argv
    if len(args) != 2:
        return dummy_func("To use, submit the number of a problem to run:\n$ python project_euler 111")
    try:
        problem_number = int(args[1])
    except ValueError:
        return dummy_func("Problem number must be an int")
    pattern = re.compile(r"^(solved|problems)\.p{:d}$".format(problem_number))
    for module_name, module in sys.modules.iteritems():
        match = pattern.match(module_name)
        if match:
            if match.group(1) == "solved":
                t0 = time.time()
                solution = module.main()
                t1 = time.time() - t0
                return dummy_func("Solution to problem {:d}: {:s}\nTime to compute: {:s} seconds".format(
                    problem_number,
                    str(solution),
                    str(t1)))
            else:
                print("Problem {:d} in progress.  Current output:".format(problem_number))
                print(module.main())
                return dummy_func("")
    return dummy_func("Cannot find problem {:d}".format(problem_number))


def __main():
    can_solve()()


if __name__ == "__main__":
    sys.exit(__main())