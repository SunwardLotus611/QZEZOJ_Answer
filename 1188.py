n = int(input())
num = list(map(int, input().split()))
tot = sum(num)
average = tot / n
print(tot, f"{average:.5f}")
