T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    map = list(map( int, input().split()))
    array = [[0] * M for _ in range(N)]
    dp = [[0] * M for _ in range(N)]
    max_value = -1

    i = 0
    while i < len(map):
        mok, namujee = i // M, i % M
        array[mok][namujee] = map[i]
        i += 1

    for i in range(N):
        dp[i][0] = array[i][0]

    for j in range(M):
        for i in range(N):
            temp = array[i][j]

            r, c = i + 1, j - 1
            if 0 <= r < N and 0 <= c < M:
                temp = max(temp, array[i][j] + dp[r][c])


            r, c = i, j - 1
            if 0 <= r < N and 0 <= c < M:
                temp = max(temp, array[i][j] + dp[r][c])


            r, c = i - 1, j - 1
            if 0 <= r < N and 0 <= c < M:
                temp = max(temp, array[i][j] + dp[r][c])

            dp[i][j] = temp
            max_value = max(temp, max_value)

    print(max_value)





