from operator import itemgetter
num = int(input())
inputEnd = list(map(int, input().split()))
pointList = []

for i in range(num):
    start = i+1
    end = inputEnd[i]
    pointList.append((start, end, abs(start - end)))

pointList.sort(key = itemgetter(2,0))

lastOne = pointList[0]
count = 1
for i in range(1, num):
    if pointList[i][0] > lastOne[0]:
        if pointList[i][1] > lastOne[1]:
            count += 1
            lastOne = pointList[i]
            print(pointList[i])

print(count)