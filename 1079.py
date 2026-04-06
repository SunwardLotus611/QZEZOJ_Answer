s = input()
c = 0
co = 0
cow = 0
for i in s:
    if i == 'C':
        c += 1
    elif i == 'O':
        co += c
    elif i == 'W':
        cow += co
print(cow)
