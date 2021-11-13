N = int(input())
array = list(map(int, input().split()))

## 구하는 것은 내림차순 이지만, 오름차순으로 구하기 위해 배열을 뒤집는다.
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if i == j:
            continue

        if array[i] > array[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))