N, M = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()
results = []
answer = 0

def binary_search(array, start, end, target):
    global answer

    while start <= end:
        mid = (start + end) // 2
        result = sum([number - mid if number - mid > 0 else 0 for number in array])

        if result < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1


binary_search(heights, 0, heights[-1], M)
print(answer)



