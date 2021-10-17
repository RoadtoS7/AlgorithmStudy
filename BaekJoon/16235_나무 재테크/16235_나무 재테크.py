from collections import deque

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
graph = [[5 for _ in range(N)]  for _ in range(N)]
initial_tree = [list(map(int, input().split())) for _ in range(M)]
trees = [[deque(list()) for _ in range(N)] for _ in range(N)]

## 방향 조심해서 추가하기!!
dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]

## init tree
for x, y, age in initial_tree:
    trees[x - 1][y - 1].append(age)

for _ in range(K):
    tree5 = []

    # 봄
    for r in range(N):
        for c in range(N):
            l = len(trees[r][c])


            if l <= 0:
                continue

            for i in range(l):
                if graph[r][c] >= trees[r][c][i]:
                    graph[r][c] -= trees[r][c][i]
                    trees[r][c][i] += 1

                    if trees[r][c][i] % 5 == 0:
                        tree5.append((r, c))

                else:
                    for _ in range(i, l):
                        age = trees[r][c].pop()
                        graph[r][c] += age // 2

                    break


    ## 가을
    for r, c in tree5:
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            trees[nr][nc].appendleft(1)

    ## 겨울
    for r in range(N):
        for c in range(N):
            graph[r][c] += A[r][c]

## 트리 개수 구하기
answer = 0
for r in range(N):
    for c in range(N):
        answer += len(trees[r][c])

print(answer)
