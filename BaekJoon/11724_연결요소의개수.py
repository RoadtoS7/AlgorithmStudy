N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
result = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(node):
    visited[node] = True
    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(new_node)


for node in range(1, N + 1):
    if not visited[node]:
        result += 1
        dfs(node)

print(result)
