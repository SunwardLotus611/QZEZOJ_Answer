from itertools import cycle
text = input().lower()
key_cycle = cycle(map(int, input()))
res = ''.join(
    chr((ord(c) - 97 + next(key_cycle)) % 26 + 97)
    if c.isalpha() else c
    for c in text
)
print(res)
