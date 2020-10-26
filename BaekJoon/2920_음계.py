from sys import stdin
data_list = list(map(int, stdin.readline().split(" ")))
ifAscending = None
for index in range(len(data_list) - 1):
    flag = (data_list[index + 1] - data_list[index] > 0)
    if ifAscending is None:
        ifAscending = flag
    else:
        if ifAscending != flag:
            break

if ifAscending == flag:
    if ifAscending:
        print("ascending")
    else:
        print("descending")
else:
    print("mixed")

