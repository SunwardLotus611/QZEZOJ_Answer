n, k = map(int, input().split())
step = [1, 1]
for i in range(2, k + 1):
    step.append(sum(step))
for i in range(k + 1, n + 1):
    step.pop(0)
    step.append(sum(step))
print(step[-1] % 100000000)
