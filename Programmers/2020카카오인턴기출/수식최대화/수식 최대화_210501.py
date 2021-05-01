import re

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    return a * b

def solution(expression):
    operator_set = {'+', '-', '*'}
    operator_pr = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ]
    exp_list = re.split(r'(\D)', expression)
    operators, numbers = [], []
    candiates= []

    for exp in exp_list:
        if exp in operator_set and exp in expression:
            operators.append(exp)
        else:
            numbers.append(int(exp))

    for ops in operator_pr:
        _numbers = numbers[:]
        _operators = operators[:]

        for op in ops:
            i = 0
            while i < len(_operators):
                if _operators[i] == op:
                    _numbers[i] = calculate(op, _numbers[i], _numbers[i + 1])
                    _operators.pop(i)
                    _numbers.pop(i + 1)
                    i -= 1
                i += 1
        candiates.append(abs(_numbers[0]))

    return sorted(candiates, reverse=True)[0]


print(solution("100-200*300-500+20"))