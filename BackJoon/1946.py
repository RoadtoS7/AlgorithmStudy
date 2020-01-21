num = int(input())
result = list()

for i in range(num + 1):
    case = int(input())
    lst = list()

    for j in range(case + 1):
        lst.append(list(map(int, input().split())))

    result.append(len(lst))
    for j in range(case + 1):
        stand = lst[j]
        for k in range(case + 1):
            if lst[k][0] > stand[0]:
                if lst[k][1] > stand[1]:
                    result[i] = result[i] - 1

for i in result:
    print(i)
