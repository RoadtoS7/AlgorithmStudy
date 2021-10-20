N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
shark = dict()
# 상어 위치 구하기
for r in range(N):
    for c in range(N):
        if graph[r][c] > 0:
            graph[r][c] -= 1
            shark[graph[r][c]] = [r, c]

# 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽
for i, sharkdir in enumerate(map(int, input().split())):
    shark[i].append(sharkdir - 1)




