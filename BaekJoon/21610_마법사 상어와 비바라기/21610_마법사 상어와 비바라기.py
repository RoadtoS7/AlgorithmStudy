N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N - 1, 0), (N - 1, 1), (N-2, 0), (N-2, 1)]
# 없음,         ←, ↖, ↑, ↗, →, ↘, ↓, ↙
d, s = [], []
cloud_dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
cloud_dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

cross_dir = [(-1, -1), (1, -1), (1, 1), (-1, 1)]

for _ in range(M):
    _d, _s = map(int, input().split())
    d.append(_d)
    s.append(_s)

for i in range(M):
    last_cloud_locations = set()
    while clouds:
        r, c = clouds.pop()
        nr, nc = (r + cloud_dr[d[i]] * s[i]) % N, (c + cloud_dc[d[i]] * s[i]) % N

        graph[nr][nc] += 1
        last_cloud_locations.add((nr, nc))

    for r, c in last_cloud_locations:
        cross_count = 0
        for dr, dc in cross_dir:
            cross_r, cross_c = r + dr, c + dc

            if cross_r < 0 or cross_r >= N or cross_c < 0 or cross_c >= N:
                continue

            if graph[cross_r][cross_c] > 0:
                cross_count += 1
        graph[r][c] += cross_count


    for i in range(N):
        for j in range(N):
            if (i, j) not in last_cloud_locations and graph[i][j] >= 2:
                clouds.append((i, j))
                graph[i][j] -= 2


res = sum(sum(i) for i in graph)
print(res)






