def F(n1, n2, cnt):
    if cnt != 0:
        return F(n2, n1 + n2, cnt - 1)
    else:
        return n1


def period(q):
    n1, n2 = 1, 1
    for i in range(0, q * q):
        n1, n2 = n2, (n1 + n2) % q
        if n1 == 1 and n2 == 1:
            return i + 1
    return 1


n, Q = map(int, input().split())
print(F(0, 1, n % period(Q)) % Q)
