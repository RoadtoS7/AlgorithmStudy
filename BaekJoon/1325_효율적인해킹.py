from collections import deque
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    end, start = map(int, input().split())
    adj[start].append(end)

def dfs(start):
    need_visit = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0
    while need_visit:
        node = need_visit.popleft()
        for next_node in adj[node]:
            if not visited[next_node]:
                count += 1
                visited[next_node] = True
                need_visit.append(next_node)
    return count

result = []
max_count = -1
for i in range(1, n + 1):
    count = dfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

for item in result:
    print(item, end=' ')
