from sys import stdin
input = stdin.readline

A, B = input().rstrip(), input().rstrip()
len_A, len_B = len(A), len(B)
dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]

result = 0
for i in range(1, len_A + 1):
    for j in range(1, len_B + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            result = max(result, dp[i][j])
print(result)
