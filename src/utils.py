from condor_function import condor_function

def condorize(f):
    return CondorFunction(f)
