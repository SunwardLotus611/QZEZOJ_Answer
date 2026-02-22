n = int(float(input()))
ans = 0
ans += n // 50 * 7
n %= 50
ans += n // 30 * 4
n %= 30
ans += n // 10
print(ans)
