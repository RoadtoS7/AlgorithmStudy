N, S, M = map(int, input().split())
volume_gaps = list(map(int, input().split()))
# 처음 시작곡의 볼륨도 저장해야하기 때문에 row의 개수는 N + 1개 이다.
playable_volume = [[0] * (M + 1) for _ in range(N + 1)]
playable_volume[0][S] = 1

for i in range(1, N + 1):
    for j in range(M + 1):
        if not playable_volume[i - 1][j]:
            continue
        if j - volume_gaps[i - 1] >= 0:
            playable_volume[i][j - volume_gaps[i - 1]] = 1

        if j + volume_gaps[i - 1] <= M:
            playable_volume[i][j + volume_gaps[i - 1]] = 1


result = -1
for i in range(M, -1, -1):
    if playable_volume[N][i]:
        result = i
        break
print(result)