def div_ab(a, b):
    if b < 0.0000001:
        raise ValueError("слишком маленькое число")
    return a / b

for x, y in ((1, 2), (324, 23423), (21, 0), (345, 1)):
    try:
        print(div_ab(x, y))
    except ValueError as e:
        print(e)
