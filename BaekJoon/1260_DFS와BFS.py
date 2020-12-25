from collections import deque

n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

for item in adj:
    item.sort()


def dfs(node):
    print(node, end=" ")
    visited[node] = True
    for node in adj[node]:
        if not (visited[node]):
            dfs(node)


def bfs(node):
    need_visit = deque([v])
    while need_visit:
        node = need_visit.popleft()
        if not (visited[node]):
            print(node, end=" ")
            visited[node] = True
            for node in adj[node]:
                if not(visited[node]):
                    need_visit.append(node)



visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
