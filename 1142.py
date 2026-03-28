n, m = map(int, input().split())
res = []
tmp = 1
for i in range(n):
    line = [chr(64 + (tmp + j) % 26) if (tmp + j) % 26 != 0 else 'Z'
            for j in range(m)]
    tmp += m
    if i % 2 != 0:
        line.reverse()
    res.append(line)
print(res)
