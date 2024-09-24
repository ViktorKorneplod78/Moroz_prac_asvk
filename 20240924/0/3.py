a = list(range(1, 11))
print(a[len(a) // 2 + 1 :: 2][::-1])

print(a[-1:len(a) // 2 - 1 : -2])
