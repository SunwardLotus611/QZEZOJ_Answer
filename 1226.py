import itertools
light = eval(input())
k = len(light)
for op in itertools.product([0, 1], repeat=k):
    flag = True
    for j in range(k):
        change = op[(j - 1) % k] ^ op[j] ^ op[(j + 1) % k]
        if light[j] ^ change != 1:
            flag = False
            break
    if flag:
        res = [i + 1 for i in range(len(op)) if op[i] == 1]
        print(res)
        break
if not flag:
    print("没有方案")
