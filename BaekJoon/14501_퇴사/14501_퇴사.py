# 끝나는 날짜가 N + 1이 되는 경우, 해당 상담을 진행할 수 없다.
N = int(input())
T, P = [], []
dp = [0] * (N + 1)
max_value = 0

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# 리스트를 거꾸로 확인
for i in range(N - 1, -1, -1):
    time = T[i] + i
    # 상담이 근무 기간내 끝나는 경우
    if time <= N:
        dp[i] = max(P[i] + dp[time], max_value)
        max_value = dp[i]

    # 상담이 근무 기간을 초과하는 경우
    else:
        dp[i] = max_value

print(max_value)