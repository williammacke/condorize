from condor_function import CondorFunction


def condorize(f):
    return CondorFunction(f)
