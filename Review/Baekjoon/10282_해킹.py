import heapq
import sys
input = sys.stdin.readline

def dijkstra(graph, start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distances[start] = 0
    while heap_data:
        current_distance, current_node = heapq.heappop(heap_data)
        if current_distance > distances[current_node]:
            continue
        for node, weight in graph[current_node]:
            cost = weight + current_distance
            if cost < distances[node]:
                distances[node] = cost
                heapq.heappush(heap_data, (cost, node))


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distances = [1e9] * (n + 1)
    for _ in range(d):
        end, start, cost = map(int, input().split())
        graph[start].append((end, cost))
    dijkstra(graph, c)
    count = 0
    max_distance = 0
    for i in distances:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
    print(count, max_distance)






