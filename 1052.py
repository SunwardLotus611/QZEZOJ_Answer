x = int(input())
weight = [20, 10, 5, 2, 1]
cnt = {20: 1, 10: 2, 5: 1, 2: 2, 1: 2}
res = []
for w in weight:
    while x >= w and cnt[w] > 0:
        res.append(w)
        x -= w
        cnt[w] -= 1
print(*(str(i) for i in res), end=" ")
