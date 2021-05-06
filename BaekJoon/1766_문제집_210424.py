import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
edge_count = [0] * (N + 1)
heap, result = [], []

for _ in range(M):
    before, after = map(int, input().split())
    graph[before].append(after)
    edge_count[after] += 1

for i in range(1, N + 1):
    if edge_count[i] == 0:
        heapq.heappush(heap, i)

while heap:
    node = heapq.heappop(heap)
    result.append(node)
    for adj in graph[node]:
        edge_count[adj] -= 1
        if edge_count[adj] == 0:
            heapq.heappush(heap, adj)

[print(problem, end=' ') for problem in result]


