from sys import setrecursionlimit

setrecursionlimit(100000)

N, M = int(input()), int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True

    for next_pos in graph[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)

dfs(1)

print(count - 1)

