import math
n = int(input())
time = 0.0
for _ in range(n):
    x, y, p = map(float, input().split())
    time += (x ** 2 + y ** 2) ** 0.5 / 50 * 2 + p * 1.5
print(math.ceil(time))
