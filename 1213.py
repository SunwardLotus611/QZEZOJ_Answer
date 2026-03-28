def check(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


res = []
for n in range(10, 100):
    if check(n) and check((n % 10) * 10 + (n // 10)):
        res.append(str(n))
print('\n'.join(res))
