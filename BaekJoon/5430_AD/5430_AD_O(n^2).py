from sys import stdin
input = stdin.readline

def get_num_arr(str):
    i, j = 0, 0
    n = len(str)
    result = []
    while i < n and j < n:
        if str[i].isnumeric():
            j = i
            while str[j].isnumeric():
                j += 1
            result.append(int(str[i:j]))
            i = j + 1
            continue

        i += 1
    return result

T = int(input())

for _ in range(T):
    operators = input().rstrip()
    N = int(input())
    nums = get_num_arr(input())
    error_flag = False

    for operator in operators:
        if operator == 'R':
            nums.reverse()
            continue
        else:
            if nums:
                nums.pop(0)
            else:
                print('error')
                error_flag = True
                break

    if not error_flag:
        print(nums)

