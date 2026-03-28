def F(n1, n2, cnt):
    if cnt != 0:
        return F(n2, n1 + n2, cnt - 1)
    else:
        return n1


n, Q = map(int, input().split())
print(F(0, 1, n) % Q)
