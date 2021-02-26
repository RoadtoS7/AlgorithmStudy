r, c = map(int, input().split())
array = []

for i in range(r):
    array.append(input())


result = 0
def dfs(x, y, set):
    global result
    set.add(array[y][x])
    result = max(result, len(set))
    if x + 1 < c and array[y][x+1] not in set:
        dfs(x + 1, y, set)
    if x - 1 >= 0 and array[y][x - 1] not in set:
        dfs(x - 1, y, set)
    if y + 1 < r and array[y + 1][x] not in set:
        dfs(x, y + 1, set)
    if y - 1 >= 0 and array[y - 1][x] not in set:
        dfs(x, y - 1, set)

dfs(0, 0, set())
print(result)

