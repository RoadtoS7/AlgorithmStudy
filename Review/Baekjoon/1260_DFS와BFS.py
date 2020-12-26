from collections import deque

n, m, v = map(int, input().split())
adj = [[] * i for i in range(n + 1)]

for _ in range(m):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

for nodes in adj:
    adj.sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for node in adj[start]:
        if not visited[node]:
            dfs(node)

def bfs(start):
    need_visit = deque([v])
    while need_visit:
        node = need_visit.popleft()
        if not visited[node]:
            print(node, end=' ')
            visited[node] = True
            for item in adj[node]:
                need_visit.append(item)

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)