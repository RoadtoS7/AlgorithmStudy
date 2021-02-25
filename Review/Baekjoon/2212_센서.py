import sys

n = int(input())
k = int(input())

# 집중국의 개수가 센서의 개수보다 많다면, 각 센서의 위치에 집중국을 두면된다.
# 따라서 집중국의 수신 가능 영역의 최소 합은 0이다.
if k >= n:
    print(0)
    sys.exit()

# 센서의 위치를 오름차순 정렬한다.
sensors = list(map(int, input().split()))
sensors.sort()

# 센서들 사이의 거리를 구한다.
distances = []
for i in range(1, n):
    distances.append(sensors[i] - sensors[i-1])
# 센서들 사이의 거리를 내림차순 정렬한다.
distances.sort(reverse=True)

# k-1개의 거리를 없앤다.
for i in range(k-1):
    distances[i] = 0

# 거리들 사이의 합이 최솟값이다.
print(sum(distances))