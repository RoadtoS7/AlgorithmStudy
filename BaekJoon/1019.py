def change(x, y, A):
    for i in range(3):
        for j in range(3):
            if A[x + i][y + j] == 0:
                A[x + i][y + j] = 1
            else:
                A[x + i][y + j] = 0
    return A

n, m = map(int, input().split())
A = [list(map(int,list(input()))) for i in range(n)]
B = [list(map(int,list(input()))) for i in range(n)]
print(A)


count = 0
for i in range(n - 3 + 1):
    for j in range(m - 3 + 1):
        if A[i][j] != B[i][j]:
            A = change(i, j, A)
            count += 1

ifSame = True
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            ifSame = False

if ifSame:
    print(count)
else:
    print(-1)

