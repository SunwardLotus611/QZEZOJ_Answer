l, r = map(int, input().split())
cnt = 0
for i in range(l, r + 1):
    if len(set(str(i))) == 2:
        cnt += 1
print(cnt)
