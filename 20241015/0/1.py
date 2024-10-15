from collections import Counter

paper = Counter(input().split())
text = Counter(input().split())
if text - paper:
    print("No")
else:
    print("AWWWWWWWWW!")
