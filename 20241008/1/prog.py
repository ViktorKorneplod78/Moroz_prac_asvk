from fractions import Fraction

def check(s, w, a_pow, a_coeff, b_pow, b_coeff):
    A, B = 0, 0
    for i in range(a_pow + 1):
        A += a_coeff[i] * (s ** i)
    for i in range(b_pow + 1):
        B += b_coeff[i] * (s ** i)

    if B != Fraction(0):
        return A/B == w
    else:
        return False

input_ = input().split(", ")
s = Fraction(input_[0])
w = Fraction(input_[1])

a_pow = int(input_[2])
a_coeff = []
i = 3
for j in range(a_pow + 1):
    a_coeff.append(Fraction(input_[i]))
    i += 1
a_coeff.reverse()

b_pow = int(input_[i])
i += 1
b_coeff = []
for j in range(b_pow + 1):
    b_coeff.append(Fraction(input_[i]))
    i += 1
b_coeff.reverse()

print(check(s, w, a_pow, a_coeff, b_pow, b_coeff))
