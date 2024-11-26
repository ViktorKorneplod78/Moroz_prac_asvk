with open("file", "rb") as f:
    f =f.read()
    print(f[len(f) // 2:], f[0:len(f) // 2])
