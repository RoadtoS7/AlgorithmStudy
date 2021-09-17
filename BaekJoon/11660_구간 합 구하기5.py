from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
gaps = [tuple(map(int, input().split())) for _ in range(M)]
S = [[0] * (N + 1) for _ in range(N + 1)]
answer = []

for i in range(N):
    for j in range(N):
        S[i + 1][j + 1] = S[i + 1][j] + S[i][j + 1] - S[i][j] + numbers[i][j]

for x1, y1, x2, y2 in gaps:
    print(S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1])


