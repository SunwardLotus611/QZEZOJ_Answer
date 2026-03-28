s = input().upper()
res = sum(ord(c) - 64 for c in s if c.isalpha())
print(res % 10001)
