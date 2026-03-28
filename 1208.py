m, k = input().split()
if int(m) % 19 == 0 and m.count('3') == int(k):
    print("YES")
else:
    print("NO")
