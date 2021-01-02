import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0

    while heap_data:
        current_distance, current_node = heapq.heappop(heap_data)
        if current_distance > distances[current_node]:
            continue

        for adj, weight in graph[current_node]:
            distance = weight + current_distance
            if distance < distances[adj]:
                distances[adj] = distance
                heapq.heappush(heap_data, (distance, adj))

for _ in range(int(input())):
    n, m, start = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    distances = [1e9] * (n + 1)
    for _ in range(m):
        x, y, cost = map(int, input().split())
        graph[y].append((x, cost))
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distances:
        if i != 1e9:
            count += 1
            if max_distance < i:
                max_distance = i
    print(count, max_distance)
