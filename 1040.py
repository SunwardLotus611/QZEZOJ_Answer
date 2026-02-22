def solve(time):
    if time > 1:
        return (solve(time - 1) + 2) ** 0.5
    else:
        return 2 ** 0.5


n = int(input())
pi = 2.0
for i in range(1, n + 1):
    pi *= (2 / solve(i))
print(round(pi, 13))
