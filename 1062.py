n = int(input())
a = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if j % i == 0:
            a[j] = 1 - a[j]
for k in range(1, n + 1):
    if a[k] == 1:
        print(k, end=' ')
