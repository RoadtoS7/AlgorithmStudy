n = int(input())
numbers = []
for _ in range(n):
    numbers.extend(list(map(int, input().split())))

left_i, right_i = [0] * n, [0] * n
for i in range(1, n):
    left_i[i] = left_i[i - 1] + i
for i in range(1, n):
    right_i[i] = right_i[i - 1] + (i + 1)


dp = [0] * (n * (n + 1) // 2)
dp[0] = numbers[0]

level = 1
for i in range(1, (n * (n + 1) // 2)):
    if left_i[level] < i < right_i[level]:
        left_index = i - (level + 1)
        right_index = i - level
        dp[i] = max(dp[left_index], dp[right_index]) + numbers[i]
        continue

    if left_i[level] == i:
        dp[i] = dp[left_i[level - 1]] + numbers[i]
        continue

    if right_i[level] == i:
        dp[i] = dp[right_i[level - 1]] + numbers[i]
        level += 1

print(max(dp))
