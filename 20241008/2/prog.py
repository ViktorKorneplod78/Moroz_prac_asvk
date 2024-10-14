from math import *

def scale(a, b, A, B, x):
    return (B - A) * (x - a) / (b - a) + A

def gra(A, B, w, h, formula):
    screen = [[" "] * w for i in range(h)]
    y_list = []
    for i in range(w):
        x = scale(0, w, A, B, i)
        y_list.append(eval(formula))
    y_max = max(y_list)
    y_min = min(y_list)

    for i in range(w):
        s = scale(y_min, y_max, 0, h - 1, y_list[i])
        screen[round(s)][i] = "*"
        if round(s - 0.25) < len(screen) and round(s - 0.25) > 0:
            screen[round(s - 0.25)][i] = "*"
        if round(s + 0.25) < len(screen) and round(s + 0.25) > 0:
            screen[round(s + 0.25)][i] = "*"
    screen.reverse()
    return screen

def show(screen):
    print("\n".join(["".join(s) for s in screen]))

W_str, H_str, A_str, B_str, formula = input().split()
W = int(W_str)
H = int(H_str)
A = int(A_str)
B = int(B_str)

show(gra(A, B, W, H, formula))
