from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_count = -1
start_point = []


for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

for start in range(1, N + 1):
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True
    count = 1

    while q:
        node = q.pop()
        for new_node in graph[node]:
            if not visited[new_node]:
                q.append(new_node)
                visited[new_node] = True
                count += 1

    if count > max_count:
        start_point = [start]
        max_count = count
    elif count == max_count:
        start_point.append(start)

start_point.sort()
for point in start_point:
    print(point, end=' ')











