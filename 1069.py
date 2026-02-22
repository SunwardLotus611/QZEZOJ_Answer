s = input().split()
num = []
k1 = k2 = ans = 0
for i in s:
    if i in '+-*/':
        k1 = num.pop()
        k2 = num.pop()
        if i == '+':
            ans = k1 + k2
        elif i == '-':
            ans = k2 - k1
        elif i == '*':
            ans = k1 * k2
        else:
            ans = k2 / k1
        num.append(ans)
    else:
        num.append(float(i))
print(round(num[0], 2))
