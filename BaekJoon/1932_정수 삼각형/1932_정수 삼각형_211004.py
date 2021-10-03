N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))

for i in range(N):
    for j in range(i + 1):
        if j == 0:
            left_up = 0
        else:
            left_up = dp[i - 1][j - 1]

        if j == i:
            right_up = 0
        else:
            right_up = dp[i - 1][j]

        dp[i][j] = dp[i][j] + max(right_up, left_up)

print(max(dp[-1]))