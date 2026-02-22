apples = list(map(int, input().split()))
h = int(input()) + 30
cnt = sum(1 for i in apples if i <= h)
print(cnt)
