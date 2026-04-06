m = int(input())
n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if m >= p[i]:
        m -= p[i]
    else:
        cnt += 1
print(cnt)
