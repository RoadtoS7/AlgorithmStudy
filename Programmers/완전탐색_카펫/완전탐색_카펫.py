def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        width, height = i + 2, yellow // i + 2
        if yellow % i == 0 and  width * height == brown + yellow:
            answer = [width, height] if width >= height else [height, width]
            break

    return answer

print(solution(8, 1))