from sys import stdin
from collections import deque
input = stdin.readline

N, M, K, X = map(int, input().rstrip('/n').split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

need_visit = deque([X])

distance = [-1] * (N + 1)
distance[X] = 0


while need_visit:
    node = need_visit.popleft()

    for next in graph[node]:
        if distance[next] == -1:
            distance[next] = distance[node] + 1
            need_visit.append(next)


isAnswerExist = False
for i, dist in enumerate(distance):
    if dist == K:
        print(i)
        isAnswerExist = True

if not isAnswerExist:
    print(-1)
