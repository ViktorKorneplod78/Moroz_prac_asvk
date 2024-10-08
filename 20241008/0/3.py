from math import sin

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def gra(a, b, w, h):
    screen = [[" "] * w for i in range(h)]
    for i in range(w):
        x = scale(0, w - 1, a, b, i)
        y = sin(x)
        s = scale(-1, 1, 0, h - 1, y)
        screen[round(s)][i] = "*"
    return screen

def show(screen):
    print("\n".join("".join(s) for s in screen))
