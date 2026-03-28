n, k = map(int, input().split())
step = [1] + [0] * n
add = [1] + [0] * n
for i in range(1, n + 1):
    l = max(0, i - k)
    step[i] = (add[i - 1] - (add[l - 1] if l > 0 else 0)) % 100000000
    add[i] = (add[i - 1] + step[i]) % 100000000
print(step[n])
