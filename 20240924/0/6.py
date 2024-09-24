arr = []
while str := input():
    arr.append(eval(str))

if not (all(len(e) == len(arr)) for e in arr):
    print("WAT")
    sys.exit(1)

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for x in arr:
    print(x)
        
