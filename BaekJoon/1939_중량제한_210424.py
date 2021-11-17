from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def bfs(c):
    queue = deque([start_node])
    # visited를 사용해도 가능한 이유:
    visited = [False] * (N + 1)
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        for adj, weight in graph[node]:
            if not visited[adj] and weight <= c:
                visited[adj] = True
                queue.append(adj)

    return visited[end_node]

start, end = 1000000000, 0

for _ in range(M):
    x, y, weight = map(int, input().split())
    graph[x].append((y, weight))
    graph[y].append((x, weight))
    start = min(start, weight)
    end = max(end, weight)

start_node, end_node = map(int, input().split())

result = start
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)