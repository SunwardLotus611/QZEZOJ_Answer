from collections import Counter
n, T = map(int, input().split())
a = eval(input())
cnt = [Counter() for i in range(n)]
for i in range(T):
    p, x = map(int, eval(input()))
    cnt[p - 1][x] += 1
res = []
for i in range(n):
    if len(cnt[i]) < a[i]:
        res.append(0)
    else:
        res.append(min(cnt[i].values()))
print(res)
