N = int(input())
points = [0] * N

for i in range(N):
    x, y = map(int, input().split())
    points[i] = (y, x)

points.sort()
for point in points:
    print(point[1], point[0])
