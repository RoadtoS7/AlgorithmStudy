from itertools import combinations

N = int(input())
graph = []
teachers = []
spaces = []
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(N):
    row = input().split()
    graph.append(row)
    for j in range(N):
        if row[j] == 'T':
            teachers.append((i, j))
        if row[j] == 'X':
            spaces.append((i, j))

def watch(r, c, direction):
    if direction == 0:
        while c >= 0:
            if graph[r][c] == 'S':
                return True
            if graph[r][c] == 'O':
                return False
            c -= 1

    if direction == 1:
        while c < N:
            if graph[r][c] == 'S':
                return True
            if graph[r][c] == 'O':
                return False
            c +=  1

    if direction == 2:
        while r >= 0:
            if graph[r][c] == 'S':
                return True
            if graph[r][c] == 'O':
                return False
            r -= 1

    if direction == 3:
        while r < N:
            if graph[r][c] == 'S':
                return True
            if graph[r][c] == 'O':
                return False
            r +=  1

    return False


def detect():
    for r, c in teachers:
        for i in range(4):
            if watch(r, c, i):
                return True
    return False

find = False

for walls in combinations(spaces, 3):
    for row, column in walls:
        graph[row][column] = 'O'

    if not detect():
        find = True
        break

    for row, column in walls:
        graph[row][column] = 'X'

if find:
    print('YES')
else:
    print("NO")









