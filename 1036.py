w = ['日', '一', '二', '三', '四', '五', '六']
date = input()
y = int(date[: 4])
m = int(date[4: 6])
d = int(date[6: 8])
if m == 1 or m == 2:
    y -= 1
    m += 12
week = (d + 2 * m + 3 * (m + 1) // 5 + y +
        y // 4 - y // 100 + y // 400 + 1) % 7
print("星期" + w[week])
