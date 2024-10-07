from math import *

def Calc(s, t, u):
    def res(x):
        y = eval(t)
        x = eval(s)
        return eval(u)
    return res

args = eval(input())
x = eval(input())
F = Calc(*args)
print(F(x))
