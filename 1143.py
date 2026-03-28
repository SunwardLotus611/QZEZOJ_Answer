n, m = map(int, input().split())
res = [[None] * m for _ in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
x, y, di = 0, 0, 0
for i in range(n * m):
    tmp = (n * m - i - 1) % 26
    res[x][y] = chr(65 + tmp)
    nx, ny = x + dx[di], y + dy[di]
    if 0 <= nx < n and 0 <= ny < m and res[nx][ny] == None:
        x, y = nx, ny
    else:
        di = (di + 1) % 4
        x, y = x + dx[di], y + dy[di]
print(res)
