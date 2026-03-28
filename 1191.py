m, n = map(int, input().split())
if m % 2 == 0:
    m = m + 1
if n % 2 == 0:
    n = n - 1
k = (n - m) // 2 + 1
ans = (m + n) * k // 2
print(ans)
