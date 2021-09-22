from sys import stdin
input = stdin.readline

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M + K)]
S = [0] * (N + 1)
is_exist_S = False
for a, b, c in commands:
    if a == 1:
        numbers[b - 1] = c
        if is_exist_S:
            for i in range(b, N + 1):
                S[i] = S[i - 1] + numbers[i - 1]
    else:
        if not is_exist_S:
            for i in range(c + 1):
                S[i] = S[i - 1] + numbers[i - 1]
            is_exist_S = True
        print(S[c] - S[b - 1])





