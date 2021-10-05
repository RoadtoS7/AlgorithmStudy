dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change_dir(d):
    if (d == 0):
        return 3
    elif (d == 1):
        return 0
    elif (d == 2):
        return 1
    elif (d == 3):
        return 2


def clean_up(r, c, cur_dir):
    row, col = r, c
    count = 1
    graph[row][col] = 2

    while True:
        check_dir = cur_dir

        for _ in range(4):
            empty = 0
            check_dir = change_dir(check_dir)
            dr, dc = dx[check_dir], dy[check_dir]
            nr, nc = row + dr, col + dc

            if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] == 0:
                count += 1
                row, col = nr, nc
                graph[nr][nc] = 2
                cur_dir = check_dir
                empty = 1
                break

        if empty == 0:
            # 후진
            if(d == 0):
                row += 1
            elif(d == 1):
                col -= 1
            elif(d == 2):
                row -= 1
            elif(d == 3):
                col += 1
            if graph[row][col] == 1:
                break

    return count


N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

res = clean_up( r, c, d)
print(res)
