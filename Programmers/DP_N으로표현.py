def solution(N, number):
    numbers_per_count = [0, {N}]
    if number in numbers_per_count[1]:
        return 1
    for count in range(2, 9):
        count_set = {int(str(N)*count)}
        for first_number_group in range(1, count // 2 + 1):
            for first_number in numbers_per_count[first_number_group]:
                for second_number in numbers_per_count[count - first_number_group]:
                    count_set.add(first_number + second_number)
                    count_set.add(first_number - second_number )
                    count_set.add(second_number - first_number )
                    count_set.add(first_number * second_number )
                    if first_number != 0:
                        count_set.add(second_number // first_number)
                    if second_number != 0:
                        count_set.add(first_number // second_number)
        if number in count_set:
            return count
        numbers_per_count.append(count_set)
    return -1