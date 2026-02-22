s = input()
k = len(s)
flag = False
res = ''
for i in range(0, k - 1):
    if ord(s[i]) == ord(s[i + 1]) - 1 and flag == False:
        res = res + s[i] + '-'
        flag = True
    elif ord(s[i]) != ord(s[i + 1]) - 1:
        res = res + s[i]
        flag = False
res += s[i + 1]
print(res)
