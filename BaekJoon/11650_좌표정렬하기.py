from sys import stdin

n = int(stdin.readline().rstrip('\n'))

points = list()
for _ in range(n):
    input = tuple(map(int, stdin.readline().rstrip("\n").split(' ')))
    points.append(input)

points = sorted(points, key= lambda x: (x[0], x[1]))

for point in points:
    print(point[0], point[1])

