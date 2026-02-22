m, n = map(int, input().split())
count = 0
for i in range(1, 10):
    for j in range(100):
        if (i * 10000 + 5006 + j * 10) % m == 0 and (i * 10000 + 5006 + j * 10) % n == 0:
            count += 1
print(count)
