x = ['五', '四', '三', '二', '一']
s = input()
n = 0
for i in range(len(s) - 1, -1, -1):
    if s[i].isdigit():
        n = abs(int(s[i]) - 5)
        break
print('周' + x[n] + "限行")
