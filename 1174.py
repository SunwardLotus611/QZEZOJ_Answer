k = int(input())
cnt = 0
n = 1
day = 0
while k > day + n:
    cnt += n * n
    day += n
    n += 1
cnt += (k - day) * n
print(cnt)
