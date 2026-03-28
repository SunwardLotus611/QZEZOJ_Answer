def horizon(array):
    for i in range(len(array)):
        array[i].reverse()
    return array


arr = horizon(list(reversed(eval(input()))))
res = list(zip(*arr))
ans = [list(i) for i in res]
print(ans)
