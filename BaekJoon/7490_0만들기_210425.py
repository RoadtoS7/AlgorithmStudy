import copy

case = int(input())


def make_operators(exp, n):
    if len(exp) == n - 1:
        operator_list.append(copy.deepcopy(exp))
    else:
        exp.append(' ')
        make_operators(exp, n)
        exp.pop()

        exp.append('+')
        make_operators(exp, n)
        exp.pop()

        exp.append('-')
        make_operators(exp, n)
        exp.pop()


for _ in range(case):
    n = int(input())
    operator_list = []
    make_operators([], n)
    numbers = [i for i in range(1, n + 1)]

    for operators in operator_list:
        result = ""
        for i in range(0, n - 1):
            result += str(numbers[i]) + operators[i]
        result += str(numbers[-1])

        if eval(result.replace(' ', '')) == 0:
            print(result)

