from sys import stdin
input = stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
targets = list(map(int, input().split()))

def binery_search_recursive(array,  start, end, target):
    if start > end:
        return 'No'

    mid = (start + end) // 2
    if array[mid] == target:
        return 'Yes'
    if array[mid] < target:
        return binery_search_recursive(array, mid + 1, end, target)
    else:
        return binery_search_recursive(array, start, mid - 1, target)
def binary_search_for(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 'Yes'

        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 'No'

for target in targets:
    print(binery_search_recursive(numbers, 0, N - 1, target))

for target in targets:
    print(binary_search_for(numbers, 0, N - 1, target))
