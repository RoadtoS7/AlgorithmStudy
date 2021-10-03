import sys
input = sys.stdin.readline

N = int(input())

T, P = [], []
dp = [0] * 1_000


for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

for i in range(0, N):
    if dp[i] > dp[i + 1]:
        dp[i + 1] = dp[i]

    if dp[i + T[i]] < dp[i] + P[i]:
        dp[i + T[i]] = dp[i] + P[i]

print(dp[N])