def horizon(array):
    for i in range(len(array)):
        array[i].reverse()
    return array


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
op = input()
for i in op:
    if i == '1':
        arr = horizon(arr)
    elif i == '2':
        arr.reverse()
for i in arr:
    print(' '.join([str(j) for j in i]))
