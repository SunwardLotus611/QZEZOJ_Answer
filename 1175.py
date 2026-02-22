from collections import Counter
s = input()
cnt = Counter(s)
print(max(cnt.values()))
