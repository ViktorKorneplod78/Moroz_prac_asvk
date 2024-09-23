n = int(input())
a = n
while a <= n + 2:
    b = n
    while b <= n + 2:
        print(a, "*", b, "=", sep = " ", end = " ")   
        
        c = a*b
        dig_sum = 0
        while c > 0:
            dig_sum += c%10
            c = int(c/10)
        
        if dig_sum == 6:
            print(":=)", end = " ")
        else:
            print(a*b, end = " ")

        b += 1
    print()
    a += 1

