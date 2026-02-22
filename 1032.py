s = input().split()
maxword = ''
maxlen = 0
for i in s:
    if len(i) > maxlen:
        maxlen = len(i)
        maxword = i
print(maxword)
