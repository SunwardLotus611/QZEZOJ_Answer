arr = [[i] for i in eval(input())]
print(arr)
while len(arr) > 1:
    tmp = [arr[-1]] if len(arr) % 2 == 1 else []
    arr = [sorted(arr[i] + arr[i + 1])
           for i in range(0, len(arr) - 1, 2)] + tmp
    print(arr)
