import glob
import os


def import_problems(fname):
    problems = []
    for f in glob.glob(os.path.join(os.path.dirname(fname), "p*.py")):
        problems.append(f.replace("/", ".").split(".")[-2])
    return problems



def can_solve(problem_number, fname):
    print(fname)
    return "p{:d}.py".format(problem_number) in os.listdir(os.path.dirname(fname))

