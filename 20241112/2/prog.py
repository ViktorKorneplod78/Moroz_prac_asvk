class InvalidInput(Exception):
    pass
class BadTriangle(Exception):
    pass

def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput()

    if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
        raise BadTriangle()

    a = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    b = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
    c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c))**0.5

while True:
    inStr = input()
    try:
        area = triangleSquare(inStr)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{area:.2f}")
        break
