l, r = map(int, input().split())
s = ''.join(list(str(i) for i in range(l, r + 1)))
print(s.count('2'))
