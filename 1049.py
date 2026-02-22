import math


def f(x, n):
    return sum(x ** i / math.factorial(i) for i in range(1, n + 1))


x = int(input())
n = int(input())
print(round(f(x, n), 13))
