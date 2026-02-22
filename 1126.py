import heapq
n = int(input())
stones = eval(input())
heapq.heapify(stones)
tot = 0
while len(stones) > 1:
    a = heapq.heappop(stones)
    b = heapq.heappop(stones)
    cost = a + b
    tot += cost
    heapq.heappush(stones, cost)
print(tot)
