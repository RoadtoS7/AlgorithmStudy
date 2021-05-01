def solutions(numbers, hand):
    number_locations = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    left_set, right_set = {1, 4, 7}, {3, 6, 9}
    left, right = (3, 0), (3, 1)
    answer = ""
    for number in numbers:
        if number in left_set:
            answer += 'L'
            left = number_locations[number]


        elif number in right_set:
            answer += 'R'
            right = number_locations[number]

        else:
            left_length = abs(number_locations[number][0] - left[0]) + abs(number_locations[number][1] - left[1])
            right_length = abs(number_locations[number][0] - right[0]) + abs(number_locations[number][1] - right[1])

            if left_length < right_length:
                answer += 'L'
                left = number_locations[number]
            elif left_length > right_length:
                answer += 'R'
                right = number_locations[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number_locations[number]
                else:
                    answer += 'R'
                    right = number_locations[number]

    return answer

print(solutions([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
