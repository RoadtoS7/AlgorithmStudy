import copy

def make_zero(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return

    array.append(' ')
    make_zero(array, n)
    array.pop()

    array.append('+')
    make_zero(array, n)
    array.pop()

    array.append('-')
    make_zero(array, n)
    array.pop()

test_count = int(input())

for i in range(test_count):
    operator_list = list()
    n = int(input())
    make_zero([], n - 1)

    integers = [i for i in range(1, n+1)]

    for operators in operator_list:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])

        if eval(string.replace(' ', '')) == 0:
            print(string)
    print()
       