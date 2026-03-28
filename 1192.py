m, n = map(int, input().split())
m = m // 17 + 1 if m % 17 != 0 else m // 17
n = n // 17 if n % 17 != 0 else n // 17
res = 17 * (m + n) * (n - m + 1) // 2
print(int(res))
