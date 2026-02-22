s = input()
t = 0
i = 2
ans = ''
while t < len(s):
    ans += s[t]
    t += i
    i += 1
for j in range(-1, -1 - len(ans), -1):
    print(ans[j], end='')
