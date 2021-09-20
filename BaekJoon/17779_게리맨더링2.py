from sys import stdin
from collections import defaultdict
input = stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

min_value = 1e9
def calc_population(x, y):
    global min_value

    district = defaultdict(int)

    for d1 in range(N):
        d2 = N - 1 - d1 - x
        if d2 < 0:
            continue

        if y - d1 < 0 or y + d2 >= N:
            continue

        for r in range(N):
            for c in range(N):
                if 0 <= r < x + d1 and 0 <= c <= y:
                    district[1] += map[r][c]
                elif 0 <= r <= x + d2 and y < c <= N:
                    district[2] += map[r][c]
                elif x + d1 <= r <= N - 1 and 0 <= c < y - d1 + d2:
                    district[3] += map[r][c]
                elif x + d2 < r <= N - 1 and y - d1 + d2 <= c <= N - 1:
                    district[4] += map[r][c]
                else:
                    district[5] += map[r][c]
        min_value = min(min_value, max(district.values()) - min(district.values()))

for i in range(N):
    for j in range(N):
        calc_population(i, j)

print(min_value + 1)


