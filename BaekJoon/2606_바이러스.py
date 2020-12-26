count = int(input())
edge_count = int(input())

adj = [[] for i in range(count + 1)]
for _ in range(edge_count):
    start, end = map(int, input().split())
    adj[start].append(end)
    adj[end].append(start)

result = 0
visited = [False] * (count + 1)
def dfs(start):
    global result
    visited[start] = True
    result += 1
    for item in adj[start]:
        if not visited[item]:
            dfs(item)

dfs(1)
print(result - 1)
