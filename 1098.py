def roman_val(s):
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tot = 0
    for i in range(len(s)):
        if i + 1 < len(s) and val[s[i]] < val[s[i + 1]]:
            tot -= val[s[i]]
        else:
            tot += val[s[i]]
    return tot


def best_len(n):
    dic = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    length = 0
    for val, char in dic:
        cnt = n // val
        length += cnt * len(char)
        n %= val
    return length


t = int(input())
for i in range(1, t + 1):
    roman = input()
    print(len(roman) - best_len(roman_val(roman)))
