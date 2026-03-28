arr = eval(input())
res = list(reversed([list(i) for i in zip(*arr)]))
print(res)
