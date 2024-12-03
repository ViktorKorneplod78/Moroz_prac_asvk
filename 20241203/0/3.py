import readline

class C:
    a, b, c = input().split()

while s := input():
    match s.split():
        case [C.a, *_] as words if "yes" in words:
            case = 1
        case [C.b]:
            case = 2
        case [C.c, *_, C.b]:
            case = 3
        case _:
            case = None

    if case:
        print(case)
