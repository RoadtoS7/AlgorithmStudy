def solution(triangle):
    memory = [[(triangle[0][0], 0)]]

    for i in range(1, len(triangle)):
        memory_element = list()
        for memory_num in memory[i - 1]:
            memory_num_column = memory_num[1]
            memory_element.append( (memory_num[0] + triangle[i][memory_num_column],  memory_num_column))
            memory_element.append((memory_num[0] + triangle[i][memory_num_column + 1], memory_num_column + 1))

        memory.append(memory_element)

    biggest_one = max(memory[-1])

    return biggest_one[0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
