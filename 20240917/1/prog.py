n = int(input())

if n%50 == 0:
    print("A +", end = " ")
else:
    print("A -", end = " ")

if n%2 == 1 and n%25 == 0:
    print("B +", end = " ")
else:
    print("B -", end = " ")

if n%8 == 0:
    print("C +")
else:
    print("C -")
