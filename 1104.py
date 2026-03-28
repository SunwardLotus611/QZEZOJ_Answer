arr = eval(input())
res = list(zip(*arr))
ans = [list(i) for i in res]
print(ans)
