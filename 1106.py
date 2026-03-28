arr = eval(input())
res = [list(i) for i in zip(*reversed(arr))]
print(res)
