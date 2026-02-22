def solve(m):
    cn = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    ten = [None, '仟', '佰', '拾', '']
    n = [None, 0, 0, 0, 0]
    ans = ''
    for i in range(4, 0, -1):
        n[i] = m % 10
        m = m // 10
    for i in range(1, 5):
        if n[i] != 0:
            ans += cn[n[i]] + ten[i]
    return ans


t = [None, '亿', '萬', '']
money = int(input())
num = [None, 0, 0, 0]
for i in range(3, 0, -1):
    num[i] = money % 10000
    money = money // 10000
for i in range(1, 4):
    if num[i] != 0:
        print(solve(num[i]) + t[i], end='')
print("圆整")
