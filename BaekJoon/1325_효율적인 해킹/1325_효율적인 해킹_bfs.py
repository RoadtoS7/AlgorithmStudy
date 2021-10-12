from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

def bfs(x):
    visited = [False] * (N + 1)
    visited[x] = True
    count = 0
    need_visit = deque([x])

    while need_visit:
        node = need_visit.popleft()

        for i in graph[node]:
            if not visited[i]:
                count += 1
                visited[i] = True
                need_visit.append(i)

    return count


for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_value = -1
max_id = []
for i in range(1, N + 1):
    res = bfs(i)
    if max_value < res:
        max_value = res
        max_id = [i]
    elif max_value == res:
        max_id.append(i)

[print(i, end=' ') for i in max_id]
