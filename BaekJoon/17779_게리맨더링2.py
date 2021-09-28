from sys import stdin
from collections import defaultdict
input = stdin.readline

N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]
total_map = 0
for lst in map:
    total_map += sum(lst)


def calc_dict_5(map, x, y, small, big):
    result = 0
    for i in range(0, small + 1):
        result += sum(map[x + i][y - i: y + i + 1])

    for i in range(1, big - small + 1):
        result += sum(map[x + small + i][y - small + i : y + small + i])

    for i in range(1, small + 1):
        result += sum(map[x + big + i][y - 2 * small + big + i : y + big - i])

    return result

def get_dict5_start_c(x, y, d1, d2, r):
    if r < x:
        return None
    elif r <= x + d1:
        diff = r - x
        return y - diff
    elif r <= x + d1 + d2:
        diff = r - (x + d1)
        return  (y - d1) + diff
    else:
        return None

def get_dict5_end_c(x, y, d1, d2, r):
    if r < x:
        return None
    elif r <= x + d2:
        diff = r - x
        return y + diff
    elif r <= x + d1 + d2:
        diff = r - (x + d2)
        return (y + d2) - diff
    else:
        return None



def calc_popluation(x, y, N):
    dict1_lst, dict2_lst, dict3_lst, dict4_lst = [], [], [], []
    min_value  = 1e9
    for d1 in range(1, y + 1):
        for d2 in range(1, N - y):
            if x + d1 + d1 >= N:
                continue

            dict1, dict2, dict3, dict4 = 0, 0, 0, 0
            for r in range(N):
                dict5_start_c = get_dict5_start_c(x, y, d1, d2, r)
                dict5_end_c = get_dict5_end_c(x, y, d1, d2, r)


                if dict5_start_c == None:
                    if r < x + d1:
                        dict1 += sum(map[r][:y + 1])
                        dict1_lst.append((r, y))
                    else:
                        dict3 += sum(map[r][:y])
                        dict3_lst.append((r, y - 1))

                else:
                    if r < x + d1:
                        dict1 += sum(map[r][:dict5_start_c])
                        dict1_lst.append((r, dict5_start_c - 1))
                    else:
                        dict3 += sum(map[r][:dict5_start_c])
                        dict1_lst.append((r, dict5_start_c - 1))

                if dict5_end_c == None:
                    if r < x + d2:
                        dict2 += sum(map[r][y + 1:])
                        dict2_lst.append((r, y + 1))
                    else:
                        dict4 += sum(map[r][y:])
                        dict4_lst.append((r, y))

                else:
                    if r <= x + d2:
                        dict2 += sum(map[r][dict5_end_c + 1:])
                        dict2_lst.append((r, dict5_end_c + 1))
                    else:
                        dict4 += sum(map[r][dict5_end_c + 1:])
                        dict4_lst.append((r, dict5_end_c + 1))


            dict5 = total_map - sum([dict1, dict2, dict3, dict4])
            diff =  max(dict1, dict2, dict3, dict4, dict5) - min(dict1, dict2, dict3, dict4, dict5)
            if min_value > diff:
                min_value = diff
                print(x, y, d1, d2)
            # min_value = min(min_value, diff)

        print(dict1_lst)
        print(dict2_lst)
        print(dict3_lst)
        print(dict4_lst)
        return min_value



# min_value = 1e9
# for i in range(N):
#     for j in range(N):
#         result =  calc_popluation(i, j, N)
#         if result:
#             min_value = min(min_value, result)


min_value = calc_popluation(2, 4, N)
print(min_value)



