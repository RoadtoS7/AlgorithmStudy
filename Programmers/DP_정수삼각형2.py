def solution(triangle):
    memory = [[(triangle[0][0], 0)]]
    top = 0

    while top < len(triangle) - 1:
        memory_element = list()
        for memory_num in memory[top]:
            memory_element.append((memory_num[0] + triangle[top + 1][memory_num[1]], memory_num[1]))
            memory_element.append((memory_num[0] + triangle[top + 1][memory_num[1] + 1], memory_num[1] + 1))
        memory.append(memory_element)
        top += 1

    biggest_one = max(memory[top], key=lambda x: x[0])
    return biggest_one[0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
