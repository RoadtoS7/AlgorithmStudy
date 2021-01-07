# 집중국의 수신 가능 영역의 길이는 수신하려는 센서간의 거리와 같다. = 이때 가장 수신 가능 영역의 길이가 최소가 된다.
# k개의 집중국을 둔다면 센서들을 인접한 것끼리 k개로 나누는 것과 같다.

import sys

n = int(input())
k = int(input())
if n <= k:
    print(0)
    sys.exit()

array = list(map(int, input().split()))
array.sort()

distances = []
for i in range(n - 1):
    distances.append(array[i + 1] - array[i])

distances.sort(reverse=True)

for i in range(k - 1):
    distances[i] = 0

print(sum(distances))