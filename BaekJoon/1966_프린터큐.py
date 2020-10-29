from heapq import heapify
from sys import stdin


def minus(data):
    return 0 - data


priority_heap = list()
case = int(stdin.readline())
for i in range(case):
    n, target = map(int, stdin.readline().split())
    priority_list = list(map(int, stdin.readline().split()))

    data_list = list()
    for index in range(n):
        data_list.append([priority_list[index], index])

    priority_list = list(map(minus, priority_list))
    heapify(priority_list)

    target_out = 1
    for i in range(n):
        data = data_list.pop(0)
        high_priority = -priority_list[0]
        if data[0] != high_priority:
            data_list.append(data)
        else:
            priority_list.pop(0)
            if data[1] == target:
                break
            else:
                target_out += 1
    print(target_out)
