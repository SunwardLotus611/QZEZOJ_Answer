n = int(input())
arr = input().split()
cnt = 0
for i in arr:
    if int(i[3]) - int(i[0]) - int(i[1]) - int(i[2]) > 0:
        cnt += 1
print(cnt)
