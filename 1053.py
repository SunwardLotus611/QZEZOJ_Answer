def sticks(num):
    dic = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    res = 0
    for i in str(num):
        res += dic[int(i)]
    return res


n = int(input()) - 4
stick_map = {}
for i in range(1112):
    c = sticks(i)
    if c not in stick_map:
        stick_map[c] = []
    stick_map[c].append(i)
cnt = 0
if n >= 0:
    stick_cnt = sorted(stick_map.keys())
    for i in stick_cnt:
        for j in stick_cnt:
            k = n - i - j
            if k in stick_map:
                for a in stick_map[i]:
                    for b in stick_map[j]:
                        c = a + b
                        if sticks(c) == k:
                            cnt += 1
print(cnt)
