from sys import stdin
from collections import deque
input = stdin.readline
N = int(input().rstrip())

students = [list(map(int, input().split())) for _ in range(N* N)]
graph = [[0] * N for _ in range(N)]
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
stud_dict = dict()


def get_infos(like_set):
    values = []

    for r in range(N):
        for c in range(N):

            if graph[r][c] != 0:
                continue

            like_count = 0
            empty_count = 0
            for dr, dc in dir:
                newr, newc = r + dr, c + dc

                if 0 <= newr < N and 0 <= newc < N:
                    if graph[newr][newc] in like_set:
                        like_count += 1
                    elif graph[newr][newc] == 0:
                        empty_count += 1

            values.append((like_count, empty_count, r, c))

    return values

def get_point(count):
    if count == 0:
        return 0
    elif count == 1:
        return 1
    elif count == 2:
        return 10
    elif count == 3:
        return 100
    else:
        return 1000

for stu in students:
    id = stu[0]
    like_set = set(stu[i] for i in range(1, 5))
    stud_dict[id] = like_set

    lst = get_infos(like_set)
    lst.sort(key= lambda x: (-x[0], -x[1], x[2], x[3]))
    nextr, nextc = lst[0][2], lst[0][3]
    graph[nextr][nextc] = id

ans = 0
for r in range(N):
    for c in range(N):
        like_set = stud_dict[graph[r][c]]
        count = 0
        for dr, dc in dir:
            new_r, new_c = r + dr, c + dc

            if 0 <= new_r < N and 0 <= new_c < N:
                if graph[new_r][new_c] in like_set:
                    count += 1

        ans += get_point(count)

print(ans)









