n, r, c = map(int, input().split(' '))

result = 0

def move_z(size, x, y):
    global result

    if size == 2:
        if x == c and y == r:
            return print(result)
        result += 1

        if x + 1 == c and y == r:
            return print(result)
        result += 1

        if x == c and y + 1 == r:
            return print(result)
        result += 1

        if x + 1 == c and y + 1 == r:
            return print(result)
        result += 1
        return

    move_z(size // 2, x, y)
    move_z(size // 2, x + size // 2, y)
    move_z(size // 2, x, y + size // 2)
    move_z(size // 2, x + size // 2, y + size // 2)

move_z(2 ** n, 0, 0)


