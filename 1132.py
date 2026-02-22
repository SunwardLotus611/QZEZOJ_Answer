def solve(a, b, c, d, x):
    f = a * x ** 3 + b * x ** 2 + c * x + d
    df = 3 * a * x ** 2 + 2 * b * x + c
    res = x - f / df
    if "%.2lf" % res != "%.2lf" % x:
        return solve(a, b, c, d, res)
    else:
        return res


n = int(input())
for _ in range(n):
    a, b, c, d, x0 = map(float, input().split())
    print("%.2lf" % solve(a, b, c, d, x0))
