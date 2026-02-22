s = input()
i = 0
j = len(s) - 1
flag = True
while i < j:
    if s[i] == s[j]:
        i += 1
        j -= 1
    else:
        flag = False
        break
if flag:
    print("是回文字符串")
else:
    print("不是回文字符串")
