a = eval(input())
k = int(input())
x = int(input())
if (k < len(a)):
    res = a[: k] + [x] + a[k: len(a)]
else:
    res = a + [x]
print(res)
