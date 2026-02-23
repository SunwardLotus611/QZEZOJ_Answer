x = int(input())
cnt = [20, 10, 10, 5, 2, 2, 1, 1]
for i in cnt:
    if x >= i:
        print(i, end=' ')
        x -= i
