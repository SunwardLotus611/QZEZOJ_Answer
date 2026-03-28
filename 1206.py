a, b = map(int, input().split())
res = int(a ** b)
print(f"{res % 1000:03d}")
