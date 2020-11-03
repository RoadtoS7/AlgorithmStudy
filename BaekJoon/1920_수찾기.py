n = int(input())
data = set(map(int, input().split(" ")))

m = int(input())
value = list(map(int, input().split(" ")))
for index in value:
    inter = {index} & data
    if len(inter) == 0:
        print(0)
    else:
        print(1)