def rbin(n, res = [1]):
    if len(res) == n:
        print(*res, sep = "")
    else:
        rbin(n, res + [0])
        rbin(n, res + [1])

rbin(9)
