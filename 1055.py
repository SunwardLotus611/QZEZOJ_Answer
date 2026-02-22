def check(n):
    i = 2
    flag = True
    while i ** 2 <= n:
        if n % i == 0:
            flag = False
        i += 1
    return flag


a, b = map(int, input().split())
ans = 0
for i in range(a, b - 1):
    if check(i) and check(i + 2):
        ans += 1
print(ans)
