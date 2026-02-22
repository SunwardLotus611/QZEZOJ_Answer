n = int(input())
flag = True
for i in range(2, round(n ** 0.5) + 1):
    if n % i == 0:
        flag = False
        break
if flag:
    print("是素数")
else:
    print("不是素数")
