L = int(input())
w = 0
l = L
maxs = 0
while w < L and l > 0:
    if l * w > maxs:
        maxs = l * w
    w += 1
    l -= 2
print(maxs)
