cnt = 1
ans = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a == cnt:
        ans = ans + 1
    cnt = cnt + 1
print(ans)
