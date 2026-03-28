n = int(input())
res = 0
tmp = 1
for i in range(1, n + 1):
    tmp *= i
    res += tmp
print(res)
