def minf(*funs):
    return lambda x: min(f(x) for f in funs)

