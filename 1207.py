h = float(input())
s = 0
h_10 = h
for i in range(1, 11):
    s += h_10
    h_10 /= 2
    if i < 10:
        s += h_10
print(f"{s:g}")
print(f"{h_10:g}")
