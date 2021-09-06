## p149

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
graph = []
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(N):
    graph.append(list(map(int, list(input().rstrip('\n')))))

def dfs(r, c):
    # 이전에 방문 여부 체크
    if graph[r][c] == 0:
        graph[r][c] = 1

        for dr, dc in dir:
            new_r, new_c = r + dr, c + dc

            # (1) 그래프 범위를 넘어가는 좌표인가?
            # (2) 이전에 방문한 좌표인가?
            # (3) 문제의 조건 상에서 방문할 수 있는 좌표인가?
            if 0 <= new_r < N and 0 <= new_c < M and graph[new_r][new_c] == 0:
                dfs(new_r, new_c)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)



