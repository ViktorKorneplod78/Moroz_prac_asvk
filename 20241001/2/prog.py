def smart_sub(op1, op2):
    if isinstance(op1, tuple) or isinstance(op1, list):
        res = []
        for i1 in op1:
            if i1 not in op2:
                res.append(i1)
        if isinstance(op1, tuple):
            return tuple(res)
        return res
    return op1 - op2

print(smart_sub(*eval(input())))
