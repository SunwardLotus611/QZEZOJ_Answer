n = int(input())
line = [1]
for _ in range(n):
    print(*(f"{x} " for x in line), sep='')
    line = [l + r for l, r in zip([0] + line, line + [0])]
