s = input()
match s.split():
    case [a, b, c] if "yes" in a:
        print("first")
    case ['', a, '']:
        print("second")
    case [a, b, c] if c == a and  b == c:
        print("third")
