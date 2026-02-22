s = input()
ans = ""
for c in s:
    if c.isalpha():
        c = c.upper()
        ans += chr((ord(c) - 61) % 26 + 65)
    elif c.isdigit():
        ans += chr((ord(c) - 50) % 10 + 48)
    else:
        ans += c
print(ans)
