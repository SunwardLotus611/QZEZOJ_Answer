s = input() + ' '
n = 0
for i in range(0, len(s) - 1):
    n += 1
    if s[i] != s[i + 1]:
        print(str(n) + s[i], end='')
        n = 0
