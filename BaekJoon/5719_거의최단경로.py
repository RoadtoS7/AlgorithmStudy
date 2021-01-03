from collections import deque
import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node]:
            distance = weight + current_distance
            if distance < distances[adjacent] and not dropped[current_node][adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

def bfs():
    q = deque()
    q.append(end)

    while q:
        now = q.popleft()
        if now == start:
            continue
        for prev, cost in reverse_graph[now]:
            if distances[now] == distances[prev] + cost:
                dropped[prev][now] = True
                q.append(prev)

while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    start, end = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y, cost = map(int, input().split())
        graph[x].append((y, cost))
        reverse_graph[y].append((x, cost))
    dropped = [[False] * (n + 1) for _ in range(n + 1)]
    distances = [1e9] * (n + 1)
    dijkstra()
    bfs()
    distances = [1e9] * (n + 1)
    dijkstra()
    if distances[end] != 1e9:
        print(distances[end])
    else:
        print(-1)

