s = input().split()
word = input()
res = [i for i in s if word in i]
print(*(res if res else ["查找无结果"]), end=' ')
