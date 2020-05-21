# 우리는 각각의 가능한 "최소 경로"를 H와 V자가 나타내는 수평 및 수직 이동의 시퀀스로 설명한다.
# HVHV
# 문자열을 사전순으로 오름차순으로 정렬하십시오.
# 가능한 경로를 V, H로 나타내고, 경로를 나타내는 문자열을 사전순으로 정렬한다.
# 그리고 key value가 0이면 정렬한 것에서  0번인덱스의 값을 반환하고, 1이면 1번 인덱스의 값을 반환한다.
# 반환 타입: 문자열
# (x, y) = 목적지
# k : key index

import itertools
from collections import OrderedDict
import collections

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def perm(lst, n):
    ret = collections.deque()

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1):
                ret.append([lst[i]] + p)

    return ret



def dfs_perm(lst, n):
    ret = []
    idx = [i for i in range(len(lst))]

    stack = []
    for i in idx:
        stack.append([i])

    while len(stack) != 0:
        cur = stack.pop()

        for i in idx:
            if i not in cur:
                temp = cur + [i]
                if len(temp) == n:
                    element = []
                    for i in temp:
                        element.append(lst[i])

                    strElement = ''.join(element)
                    ret.append(strElement)

                else:
                    stack.append(temp)
    ret = list(set(ret))
    return ret

def getSafePaths(journeys):
    safePaths = collections.deque()
    for journey in journeys:
        x, y, k = map(int, journey.split())
        hvs = collections.deque()
        for i in range(x):
            hvs.append('H')
        for i in range(y):
            hvs.append('V')

        resultPerm = itertools.permutations(hvs)
        unique_list = list(OrderedDict(zip(resultPerm, itertools.repeat(None))))
        print(unique_list)

        # resultPerm = perm(hvs, x + y)
        # print(resultPerm)
        # resultPerm = dfs_perm(hvs, x+y)
        # resultPerm = list(set(itertools.permutations(hvs)))
        # resultPerm = itertools.permutations(hvs)
        # unique_list = list(OrderedDict(zip(resultPerm, itertools.repeat(None))))

        # resultPerm = merge_sort(resultPerm)
        # print(resultPerm)
        # print(' k:%d, len(resultPerm) %d' %(k, len(resultPerm)))
        # safePaths.append(''.join(unique_list[k]))
    return safePaths

# journeys_count = int(input().strip())
# journeys = []

# for _ in range(journeys_count):
#         journeys_item = input()
#         journeys.append(journeys_item)
#
# result = getSafePaths(journeys)
# print(result)
result = getSafePaths(['2 2 2', '2 2 3'])
print(result)