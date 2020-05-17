count = int(input())
endPoints = list(map(int,input().split()))

lowDirections = []
bigDirections = []

if endPoints[0] == 1:
    lowDirections.append(endPoints[0])
    bigDirections.append(endPoints[0])
else:
    bigDirections.append(endPoints[0])


for i in range(1, count):
    if endPoints[i] == i+1:
        lowDirections.append(endPoints[i])

        if bigDirections[-1] < endPoints[i]:
               bigDirections.append(endPoints[i])
    else:
        if endPoints[i] > i+1:
            if bigDirections[-1] < endPoints[i]:
                bigDirections.append(endPoints[i])
        else:
            if len(lowDirections) == 0 or lowDirections[-1] < endPoints[i]:
                lowDirections.append(endPoints[i])

biggerEndCount = 0
if len(lowDirections) > len(bigDirections):
    biggerEndCount = len(lowDirections)
else:
    biggerEndCount = len(bigDirections)

print(biggerEndCount)