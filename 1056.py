def prime(n):
    i = 2
    flag = True
    while i ** 2 <= n:
        if n % i == 0:
            flag = False
        i += 1
    return flag


def loop(temp):
    l = len(temp)
    flag = True
    for i in range(l - 1):
        if temp[i] != temp[0 - i - 1]:
            flag = False
    return flag


n_1, n_2 = map(int, input().split())
ans = 0
for i in range(n_1, n_2 + 1):
    if prime(i) and loop(str(i)):
        ans += 1

print(ans)
