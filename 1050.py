n = int(input())
cnt = n + 1
while True:
    if cnt % 5 == 1 and cnt % 7 == 2 and cnt % 8 == 3:
        print(cnt)
        break
    cnt += 1
