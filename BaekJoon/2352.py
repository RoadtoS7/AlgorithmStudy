numCount = int(input())
endNum = input().split()

maxCount = -1


def checkInside(matchList, end):
    global maxCount, numCount

    if end == numCount - 1:
        return

    for j in range(end + 1, numCount):
        if j == numCount - 1:
            if maxCount < len(matchList):
                maxCount = len(matchList)
                return
        if matchList[-1] < endNum[j]:
            checkInside(matchList + endNum[j], j)



for i in range(0, 6):
    numList = ""
    numList += str(i)

    checkInside(numList, i)

print(maxCount)
