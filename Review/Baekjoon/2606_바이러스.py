n, m = int(input()), int(input())

graph = [[] for _ in range(n + 1)]
need_visit = [1]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(new_node):
    global count
    count += 1
    visited[new_node] = 1

    for node in graph[new_node]:
        if not visited[node]:
            dfs(node)

dfs(1)
print(count - 1)

