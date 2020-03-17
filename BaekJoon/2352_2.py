endCount = int(input())
endPoints = list(map(int, input().split()))
endPointLst = []

for i in range(len(endPoints)):
    endPointLst.append((i, endPoints[i]))

endPointLst = sorted(endPointLst, key = lambda x:x[0])
endPointLst = sorted(endPointLst, key = lambda x:x[1])

print(endPointLst)
