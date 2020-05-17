import sys
import collections
def quickSort(a, start, end):# 재귀함수용 함수 선언(리스트, 시작인덱스, 종료인덱스)
    # print(a)
    if start < end: # 시작 인덱스 보다 끝 인덱스가 클 경우
        left = start # left 변수에 시작 인덱스 할당
        pivot = a[end] #  //pivot 값은 a리스트에 마지막 원소 값
        for i in range(start, end): # 시작인덱스부터 끝 원소까지 반복
            if a[i] < pivot: # 리스트 인덱스 값이 pivot 값보다 작을 경우라면
                a[i], a[left] = a[left], a[i] #  해당 인덱스와 left인덱스  swap
                left += 1 # 인덱스 하나 증가 시켜주기(자리를 옮겨가며 비교해야 하기 때문에)
        a[left] , a[end] = a[end], a[left] # left인덱스와 끝 인덱스 swap
        print(left)
        quickSort(a, start, left-1) # 재귀 호출 (리스트, 시작 인덱스, left-1)
        quickSort(a, left+1, end) # 재귀 호출 (리스트, left+1, 종료인덱스)
count = int(sys.stdin.readline())
numList = collections.deque()


numList = collections.deque([int(sys.stdin.readline()) for i in range(count)])
start = 0
end = count - 1
if start < end:
    left = start
    pivot = numList[start + end // 2]
    for i in range(start, end):
        if numList[i] < pivot:
            numList[i], numList[left] = numList[left], numList[i]
            left += 1
    numList[left], numList[end] = numList[end], numList[left]



for i in range(count):
    print(numList[i])


    # if len(numList) == 0:
    #     numList.append(num)
    # else:
    #     if numList[-1] <= num:
    #         numList.append(num)
    #     elif numList[0] >= num:
    #         numList.appendleft(num)
    #     else:
    #         firstIdx = 0
    #         endIdx = len(numList) - 1
    #         while firstIdx < endIdx:
    #             midIdx = firstIdx + endIdx // 2
    #             if numList[midIdx] > num:
    #                 endIdx = midIdx - 1
    #             elif numList[midIdx] < num:
    #                 startIdx = midIdx + 1
    #         numList.insert(firstIdx, num)
    #
    #
    #
