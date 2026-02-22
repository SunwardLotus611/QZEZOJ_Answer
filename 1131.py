n = int(input())
stu = []
for i in range(n):
    h, opt = map(int, input().split())
    stu.append((opt, h))
stu.sort()
res = [s[1] for s in stu]
print(res)
