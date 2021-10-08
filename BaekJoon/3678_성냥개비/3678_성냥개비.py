import sys

N = int(input())

min_nums = [sys.maxsize] * 101
suffix = ["1", "7", "4", "2", "0", "8"]

def get_max(count):
    res = ['1' for _ in range(count // 2)]
    if count & 1 == 1:
        res[0] = '7'
    return ''.join(res)

def set_min():
    min_nums[2] = 1
    min_nums[3] = 7
    min_nums[4] = 4
    min_nums[5] = 2
    min_nums[6] = 6
    min_nums[7] = 8
    min_nums[8] = 10

    for i in range(9, 101):
        for j in range(2, 8):
            cur = str(min_nums[i - j]) + suffix[j - 2]
            min_nums[i] = min(int(cur), min_nums[i])




set_min()
for _ in range(N):
    count = int(input())
    max_num = get_max(count)
    min_num = min_nums[count]
    print(min_num, max_num)



