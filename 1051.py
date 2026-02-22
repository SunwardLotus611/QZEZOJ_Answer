totLen, longLen, shortLen = map(float, input().split())
longNum_min = 0
shortNum_min = 0
leftLen_min = totLen
longNum = 0
shortNum = 0
leftLen = totLen
while shortNum * shortLen <= totLen:
    leftLen = totLen - shortNum * shortLen
    longNum = leftLen // longLen
    leftLen %= longLen
    if leftLen <= leftLen_min:
        leftLen_min = leftLen
        longNum_min = longNum
        shortNum_min = shortNum
    shortNum += 1
print("长线材" + str(int(longNum_min)), "短线材" + str(int(shortNum_min)))
