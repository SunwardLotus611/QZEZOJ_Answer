s = input() + ' '
ans = 0
temp = 0
for i in s:
    if i.isdigit():
        temp = temp * 10 + int(i)
    else:
        ans += temp
        temp = 0
print(ans)
