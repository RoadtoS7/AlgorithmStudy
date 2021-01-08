n, B = int(input()), list(map(int, input().split()))

A = [0 for _ in range(n)]
A[0] = B[0]
for i in range(1, n):
    A[i] = B[i] * (i + 1) - sum(A)

for number in A:
    print(number, end=' ')
