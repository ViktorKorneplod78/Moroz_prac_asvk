a, b, c = eval(input())
print(min(a, b, c) > 0 and max(a, b, c) < sum((a, b, c)) - max(a, b, c))
