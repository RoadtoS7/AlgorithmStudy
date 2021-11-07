from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(100000)

def dfs(x):
    global count
    if not visited[x]:
        visited[x] = True
        count += 1

    for j in graph[x]:
        if not visited[j]:
            dfs(x)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_count, max_id = 0, []

for i in range(1, N + 1):
    count = 0
    visited = [False] * (N + 1)
    dfs(i)
    if max_count < count:
        max_id = [i]
        max_count = count
    elif max_count == count:
        max_id.append(i)

[print(i, end =' ') for i in max_id]

