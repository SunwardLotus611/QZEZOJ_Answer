k = int(input())
n = 2 ** k
table = [[0] * n for _ in range(n)]
table[0][0] = 1
m = 1
for _ in range(k):
    for i in range(m):
        for j in range(m):
            table[i][j + m] = table[i][j] + m
            table[i + m][j] = table[i][j + m]
            table[i + m][j + m] = table[i][j]
    m *= 2
for i in table:
    print(i)
