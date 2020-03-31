# 그리디로 푸는 경우에는 현재 위치에서 같지 않으면 연산을 적용해주면된다.
def change(i, j, A):
    for x in range(3):
        for y in range(3):
            if A[i + x][j + y] == 0:
                A[i + x][j + y] = 1
            else:
                A[i + x][j + y] = 0
    return A


n, m = map(int, input().split())
A = [list(map(int, list(input()))) for i in range(n)]
B = [list(map(int, list(input()))) for i in range(n)]

count = 0

for i in range(n - 3 + 1):
    for j in range(m - 3 + 1):
        if A[i][j] != B[i][j]:
            A = change(i, j, A)
            count += 1

sameFlag = True
for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            sameFlag = False

if sameFlag:
    print(count)
else:
    print(-1)
