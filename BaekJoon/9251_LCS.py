x, y = input(), input()

dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
# 가장 처음에 위치하는 단어를 가지고 비교할 때 [0]의 값이 필요하다.

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(x)][len(y)])
