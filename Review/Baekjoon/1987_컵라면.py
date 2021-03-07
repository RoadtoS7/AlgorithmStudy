import heapq
from sys import stdin
input = stdin.readline

N = int(input())
problems = []
solved = []

for _ in range(N):
    deadline, cup_count = map(int, input().split())
    problems.append((deadline, cup_count))

problems.sort()
for i in range(N):
    deadline = problems[i][0]
    heapq.heappush(solved, problems[i][1])
    if deadline < len(solved):
        heapq.heappop(solved)

print(sum(solved))
