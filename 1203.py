a, b, c = map(int, input().split())
x = 2
while True:
    if a % x == b % x == c % x:
        print(x)
        break
    x += 1
