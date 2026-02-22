n = int(input())
f = []
i = 2
flag = True
while n > 1:
    if n % i == 0:
        if flag:
            f.append(i)
            flag = False
        n /= i
    else:
        i += 1
        flag = True
for j in f:
    print(j, end=' ')
