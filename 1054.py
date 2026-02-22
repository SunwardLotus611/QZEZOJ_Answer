def prime(n):
    i = 2
    flag = True
    while i ** 2 <= n:
        if n % i == 0:
            flag = False
        i += 1
    return flag


num = int(input())
a = int(num / 2)
b = int(num / 2)
ans_1 = 0
ans_2 = 0
while a > 1:
    if prime(a) and prime(b):
        ans_1 = a
        ans_2 = b
    a -= 1
    b += 1
print(str(num) + '=' + str(ans_1) + '+' + str(ans_2))
