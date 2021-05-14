def get_current_location(str):
    c = ord(str[0]) - ord('A') + 1
    r = int(str[1])
    return (r, c)


def get_column_alphabet(column):
    return chr(ord('A') + column - 1)


R, C = 8, 8

directions = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0),
              'RT': (1, 1), 'LT': (1, -1), 'RB': (-1, 1), 'LB': (-1, -1)}

king, stone, N = input().split()
N = int(N)
king_r, king_c = get_current_location(king)
stone_r, stone_c = get_current_location(stone)

for _ in range(N):
    dr, dc = directions[input()]
    new_r, new_c = king_r + dr, king_c + dc
    if 1 <= new_r <= R and 1 <= new_c <= C:
        if new_r == stone_r and new_c == stone_c:
            new_stone_r, new_stone_c = stone_r + dr, stone_c + dc
            if 1 <= new_stone_r <= R and 1 <= new_stone_c <= C:
                king_r, king_c = new_r, new_c
                stone_r, stone_c = new_stone_r, new_stone_c
        else:
            king_r, king_c = new_r, new_c

print(get_column_alphabet(king_c), king_r, sep='')
print(get_column_alphabet(stone_c), stone_r, sep='')
