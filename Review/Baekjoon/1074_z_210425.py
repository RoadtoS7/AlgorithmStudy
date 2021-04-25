directions = [(0, 0), (0, 1), (1, 0), (1, 1)]
def visit(x, y, width):
    global k
    if width == 2:
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if new_x == c and new_y == r:
                print(k)
                return
            k += 1
    else:
        new_width = width // 2
        visit(x, y, new_width)
        visit(x + width // 2, y, new_width)
        visit(x, y + width // 2, new_width)
        visit(x + width // 2, y + width // 2, new_width)

N, r, c = map(int, input().split())
k = 0
visit(0, 0, 2 ** N)
