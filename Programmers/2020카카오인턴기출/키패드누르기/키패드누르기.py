def solution(numbers, hand):
    left, right = '*', '#'
    left_numbers = {'1', '4', '7'}
    right_numbers = {'3', '6', '9'}
    keypad = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1),
              '9': (2, 2), '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    answer = ''
    numbers = list(map(str, numbers))
    for number in numbers:
        if number in left_numbers:
            answer += 'L'
            left = number
            continue

        if number in right_numbers:
            answer += 'R'
            right = number
            continue

        left_distance = abs(keypad[number][0] - keypad[left][0]) + abs(keypad[number][1] - keypad[left][1])
        right_distance = abs(keypad[number][0] - keypad[right][0]) + abs(keypad[number][1] - keypad[right][1])

        if left_distance > right_distance:
            answer += 'R'
            right = number

        elif left_distance < right_distance:
            answer += 'L'
            left = number
        else:
            if hand == 'left':
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
