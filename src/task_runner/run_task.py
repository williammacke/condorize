from condor_function import Task
import sys
import pickle


def run_task(t: Task):
    return t._f(*t._args, **t._kwargs)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Pease provide at least 2 arguments")
        exit()
    with open(sys.argv[1], 'rb') as f:
        t = pickle.load(f)
    result = run_task(t)
    with open(sys.argv[2], 'wb') as f:
        pickle.dump(result, f)
