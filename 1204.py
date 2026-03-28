a, b, n = map(int, input().split())
res = ((a % b * (10 ** (n - 1) % b)) % b) * 10 // b
print(res)
