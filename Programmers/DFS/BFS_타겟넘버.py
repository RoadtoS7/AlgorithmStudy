def DFS(index, numbers, target, value):
    global answer
    if index == len(numbers) and value == target:
        answer += 1
        return
    if index == len(numbers):
        return

    DFS(index + 1, numbers, target, value + numbers[index])
    DFS(index + 1, numbers, target, value - numbers[index])

def solution(numbers, target):
    global answer
    answer = 0
    DFS(0, numbers, target, 0)
    return answer