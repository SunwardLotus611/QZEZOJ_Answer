s = input()
upper = False
lower = False
num = False
for i in s:
    if 'A' <= i <= 'Z':
        upper = True
    if 'a' <= i <= 'z':
        lower = True
    if i.isdigit():
        num = True
if len(s) >= 6 and upper and lower and num:
    print("符合要求")
else:
    print("不符合要求")
