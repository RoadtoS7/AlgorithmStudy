from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + numbers[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(S[j] - S[i - 1])