arr = eval(input())
t = int(input())
for _ in range(t):
    x, p = map(int, input().split())
    arr.insert(p, x)
print(arr)
