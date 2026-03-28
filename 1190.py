n = int(input())
gold, silver, bronze = 0, 0, 0
for i in range(n):
    g, s, b = map(int, input().split())
    gold += g
    silver += s
    bronze += b
tot = gold + silver + bronze
print(gold, silver, bronze, tot)
