sum_pos = 0
while (n := int(input())) > 0:
    sum_pos += n
    if sum_pos > 21:
        print(sum_pos)
        break
else:
    print(n)
