def esum(N, one):
    res = one
    fct = one
    for i in range(1, N):
        fct *= i
        res += one/fct
    return res
