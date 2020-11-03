# n = int(input())
# data = set(map(int, input().split(" ")))
#
# m = int(input())
# value = list(map(int, input().split(" ")))
# for index in value:
#     inter = {index} & data
#     if len(inter) == 0:
#         print(0)
#     else:
#         print(1)

n = int(input())
array = set(map(int, input().split(" ")))
m = int(input())
x = list(map(int, input().split(" ")))

for i in x:
    if i in array:
        print(1)
    else:
        print(0)