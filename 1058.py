n = int(input())
for i in range(1, n):
    print(' ' + ' '.join([str(j) for j in range(1, i + 1)]))
for i in range(n, 0, -1):
    print(' ' + ' '.join([str(j) for j in range(1, i + 1)]))
