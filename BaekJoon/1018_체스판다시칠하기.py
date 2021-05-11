def count(start_color, chess, r, c):
    row_color = start_color
    column_color = start_color
    count = 0
    for i in range(r, r + 8):
        for j in range(c, c + 8):
            if chess[i][j] != column_color:
                count += 1
            column_color = change_color(column_color)

        row_color = change_color(row_color)
        column_color = row_color
    return count


def change_color(now_color):
    if now_color == 'B':
        return 'W'
    else:
        return 'B'


N, M = map(int, input().split())
chess = []
for i in range(N):
    chess.append(input())

min_count = 65

i = 0
while i + 8 <= N:
    j = 0
    while j + 8 <= M:
        min_count = min(count('B', chess, i, j), count('W', chess, i, j), min_count)
        j += 1
    i += 1

print(min_count)
