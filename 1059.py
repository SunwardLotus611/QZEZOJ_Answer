s = input()
pos = 0
n = 1
maxs = 0
for i in range(len(s) - 1):
    if s[i] < s[i + 1]:
        n += 1
    else:
        if n > maxs:
            maxs = n
            pos = i
        n = 1
if n > maxs:
    maxs = n
    pos = i + 1
print(s[pos + 1 - maxs: pos + 1])
