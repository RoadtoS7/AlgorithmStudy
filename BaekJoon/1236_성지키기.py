n, m = map(int, input().split(' '))

castle = list()
for _ in range(n):
    castle.append(input())


i_set = set()
j_set = set()
for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            i_set.add(i)
            j_set.add(j)

i_need = n - len(i_set)
j_need = m - len(j_set)

if i_need > j_need:
    print(i_need)
else:
    print(j_need)
