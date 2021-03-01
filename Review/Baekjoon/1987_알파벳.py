dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())

table = [""] * r
for i in range(r):
    table[i] = input()

def bfs(x, y):
    global result
    q = set()
    q.add((x, y,  table[y][x]))
    ## x, y까지 왔을 때의 경로를 저장한다.

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < c and new_y >= 0 and new_y < r and table[new_y][new_x] not in step:
                q.add((new_x, new_y, step + table[new_y][new_x]))


result = 0
bfs(0, 0)
print(result)