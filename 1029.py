s = input()
u = s.upper()
l = s.lower()
ans = ""
for i in range(len(s)):
    if s[i] == u[i]:
        ans += l[i]
    else:
        ans += u[i]
print(ans)
