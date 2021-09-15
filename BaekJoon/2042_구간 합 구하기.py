N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]

commands = []
for _ in range(M + K):
    a, b, c = map(int, input().split())
    commands.append((a, b, c))

sum_list = [0] * (N)
sum_list[0] = numbers[0]

for i in range(1, N):
    sum_list[i] = sum_list[i - 1] + numbers[i]

for a, b, c in commands:
    if a == 1:
        numbers[b - 1] = c
        for i in range(b - 1, N):
            sum_list[i] = sum_list[i - 1] + numbers[i]
    else:
        print(sum_list[c - 1] - sum_list[b - 2])



