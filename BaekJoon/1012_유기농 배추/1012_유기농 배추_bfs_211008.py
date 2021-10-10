from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for _ in range(K):
        c, r = map(int, input().split())
        graph[r][c] = 1

    for i in range(N):
        for j in range(M):

            if graph[i][j] and not visited[i][j]:
                count += 1
                need_visit = deque([(i, j)])
                visited[i][j] = True

                while need_visit:
                    r, c = need_visit.popleft()

                    for k in range(4):
                        new_r, new_c = r + dr[k], c + dc[k]

                        if new_r < 0 or new_c <0 or new_r >= N or new_c >= M:
                            continue

                        if graph[new_r][new_c] and not visited[new_r][new_c]:
                            visited[new_r][new_c] = True
                            need_visit.append((new_r, new_c))

    print(count)


