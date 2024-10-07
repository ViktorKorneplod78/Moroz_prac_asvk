def Pairto(*pairs):
    res = []
    for pair in pairs:
        for i in pairs:
            if pair[0] <= i[0] and pair[1] <= i[1] and (pair[0] < i[0] or pair[1] < i[1]):
                break
        else:
            res.append(pair)
    return tuple(res)

in_tuple = eval(input())
print(Pairto(*in_tuple))
