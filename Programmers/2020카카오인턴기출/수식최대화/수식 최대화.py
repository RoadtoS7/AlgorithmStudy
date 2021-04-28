def calculator(operator, a, b):
    if operator == '+':
        return a + b
    if operator == '*':
        return a * b
    return a - b

def solution(expression):
    answer = 0
    numbers, operators = [], []
    operator_set = {'+', '-', '*'}
    priority_operator = [
        ['+', '-', '*'],
        ['-', '+', '*'],
        ['+', '*', '-'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '-', '+']
    ]
    last_index = 0


    for i in range(len(expression)):
        if expression[i] in operator_set:
            numbers.append(int(expression[last_index:i]))
            operators.append(expression[i])
            last_index = i + 1
    numbers.append(int(expression[last_index:]))

    for ops in priority_operator:
        temp_numbers = numbers[:]
        temp_operators = operators[:]

        for op in ops:
            i = 0
            while i < len(temp_operators):
                if temp_operators[i] == op:
                    a = temp_numbers[i]
                    b = temp_numbers.pop(i + 1)
                    temp_numbers[i] = calculator(op, a, b)
                    temp_operators.pop(i)
                    i -= 1
                i += 1

        answer = max(abs(temp_numbers[0]), answer)

    return answer


print(solution("100-200*300-500+20"))
