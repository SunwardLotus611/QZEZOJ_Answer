_id = input()
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
codes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
body = _id[: 17]
code = _id[-1].upper()
tot = sum(int(digit) * weight for digit, weight in zip(body, weights))
if codes[tot % 11] == code:
    print("身份证合法")
else:
    print("身份证不合法")
