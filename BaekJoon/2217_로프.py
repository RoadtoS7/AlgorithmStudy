import heapq
from sys import stdin
input = stdin.readline

n = int(input())
ropes = []
for _ in range(n):
    heapq.heappush(ropes, int(input()))

max_weight = 0
while ropes:
    min_rope = heapq.heappop(ropes)
    weight = min_rope * n
    if weight > max_weight:
        max_weight = weight
    n -= 1

print(max_weight)


