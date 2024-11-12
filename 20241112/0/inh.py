#наследование

class A:
    v = 1

class B(A):
    v = 2

b = B()
b.v = 3
print(b.v) # 3
del b.v
print(b.v) # 2
del B.v
print(b.v) # 1
