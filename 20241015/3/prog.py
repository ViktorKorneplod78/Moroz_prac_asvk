from collections import Counter

W = int(input())
text = ""
while s := input():
    for c in s.lower():
        if c.isalpha():
            text += c
        else:
            text += ' '

cnt = Counter(text.split())
max_cnt = 0
ans = []
for word in cnt:
    if len(word) == W:
        max_cnt = max(max_cnt, cnt[word])
for word in cnt:
    if len(word) == W and cnt[word] == max_cnt:
        ans.append(word)
print(*ans, sep = " ")
