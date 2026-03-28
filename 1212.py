primes = [True] * (1001)
primes[0] = primes[1] = False
for p in range(2, int(1000 ** 0.5) + 1):
    if primes[p]:
        for i in range(p * p, 1001, p):
            primes[i] = False
res = [str(i) for i in range(10, 1001) if primes[i] and str(i) == str(i)[:: -1]]
print('\n'.join(res))
