s = input()
flag = True
for i in s:
    if i == '_' or i.isdigit() or i.isalpha():
        continue
    else:
        flag = False
        break
if s[0].isdigit():
    flag = False
if flag:
    print("是")
else:
    print("否")
