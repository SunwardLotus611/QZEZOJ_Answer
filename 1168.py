m, t = input().split()
ans = sum(1 for i in range(1, int(m) + 1) if t not in str(i))
print(ans)