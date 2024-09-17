while string := input():
    if eval(string) % 2 == 0:
        print(string)
    if eval(string) == 13:
        break
else:
    print("Congrats")
