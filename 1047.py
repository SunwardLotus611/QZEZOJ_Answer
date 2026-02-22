s = input()
ans = ""
for i in s:
    if i.isalpha():
        i = i.upper()
        ans += chr((ord(i) - 61) % 26 + 65)
    elif i.isdigit():
        ans += chr((ord(i) - 50) % 10 + 48)
    else:
        ans += i
print(ans)
