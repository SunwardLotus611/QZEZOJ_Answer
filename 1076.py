import re
n = int(input())
stu = []
maxcnt = 0
for i in range(n):
    name = input()
    sign = input()
    stu.append([name, len(re.findall(r'(?=(sos))', sign))])
    if stu[i][1] > maxcnt:
        maxcnt = stu[i][1]
print(' '.join(j[0] for j in stu if j[1] == maxcnt))
print(maxcnt)
