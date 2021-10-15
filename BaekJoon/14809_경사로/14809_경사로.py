def check_if_can_cross(lst):
    empty = [True] * N

    for i in range(0, N - 1):
        if lst[i] == lst[i + 1]:
            continue

        if abs(lst[i] - lst[i + 1]) > 1:
            return False

        if lst[i] > lst[i + 1]:
            for j in range(1, L + 1):
                k = i +j
                if k < 0 or k >= N: return False
                if lst[i + 1] != lst[k]: return False
                if not empty[k]: return False
                empty[k] = False

        if lst[i] < lst[i + 1]:
            for j in range(0, L):
                k = i - j
                if k < 0 or k >= N: return False
                if lst[i] != lst[k]: return False
                if not empty[k]: return False
                empty[k] = False

    return True

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0

# 행 검사
for row in graph:
    if check_if_can_cross(row):
        count += 1

# 행 검사
for c in range(N):
    column = []
    for r in range(N):
        column.append(graph[r][c])

    if check_if_can_cross(column):
        count += 1

print(count)
