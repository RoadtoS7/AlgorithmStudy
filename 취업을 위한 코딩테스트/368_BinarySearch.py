N = int(input())
numbers = list(map(int, input().split()))

def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        if array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1

print(binary_search(numbers, 0, N - 1))
