bucket = [0] * 16
socks = input().split()
sum = 0
for i in socks:
    bucket[int(i)] += 1
for i in bucket:
    sum += i // 2
print(sum)
