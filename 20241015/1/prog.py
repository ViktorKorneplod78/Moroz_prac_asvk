pairs = set()
first = ""
for i in input():
    if i.isalpha() and len(first) > 0 and first.isalpha():
        pairs.add((first.upper(), i.upper()))
    first = i
print(len(pairs))
