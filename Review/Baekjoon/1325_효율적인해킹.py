from collections import deque

N, M = map(int, input().split())
graph = [[]  for _ in range(N + 1)]
visited = [[False] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)


def bfs(new_node):
    q = deque([new_node])
    visited = [False] * (N + 1)
    visited[new_node] = True
    count = 1
    while q:
        v = q.pop()
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True
                count += 1
    return count

result = []
max_value = -1
for i in range(1, N + 1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=' ')


