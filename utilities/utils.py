import glob
import os
import re
import time
import sys


def import_problems(fname):
    problems = []
    for f in glob.glob(os.path.join(os.path.dirname(fname), "p*.py")):
        problems.append(f.replace("/", ".").split(".")[-2])
    return problems


def can_solve(args):
    if len(args) != 2:
        print("To use, submit the number of a problem to run:\n$ python project_euler 111")
        return
    try:
        problem_number = int(args[1])
    except ValueError:
        print("Problem number must be an int")
        return
    pattern = re.compile(r"^(solved|problems)\.p{:d}$".format(problem_number))
    for module_name, module in sys.modules.iteritems():
        match = pattern.match(module_name)
        if match:
            if match.group(1) == "solved":
                t0 = time.time()
                solution = module.main()
                t1 = time.time() - t0
                print("Solution to problem {:d}: {:s}\nTime to compute: {:s} seconds".format(
                    problem_number,
                    str(solution),
                    str(t1)))
                return
            else:
                print("Problem {:d} in progress.  Current output:".format(problem_number))
                print(module.main())
                return
    print("Cannot find problem {:d}\n{:s}".format(problem_number, all_problems()))


def all_problems():
    pattern = re.compile(r"^(solved|problems)\.p(\d+)$")
    available = {"solved": [], "problems": []}

    for module_name, module in sys.modules.iteritems():
        match = pattern.match(module_name)
        if match:
            available[match.group(1)].append(int(match.group(2)))

    avail_str = "The following problems are solved:\n\t"
    avail_str += "\n\t".join(map(str, sorted(available["solved"])))
    if available["problems"]:
        avail_str += "\nThe following problems are in progress:\n\t"
        avail_str += "\n\t".join(map(str, sorted(available["problems"])))
    return avail_str