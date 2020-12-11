def split(data):
    if len(data) == 1:
        return data
    mid = len(data) // 2
    left_data = split(data[:mid])
    right_data = split(data[mid:])
    return merge_sort(left_data, right_data)

def merge_sort(left_data, right_data):
    i, j = 0, 0
    result = list()

    while i < len(left_data) and j < len(right_data):
        if left_data[i] < right_data[j]:
            result.append(left_data[i])
            i += 1
        else:
            result.append(right_data[j])
            j += 1

    while i < len(left_data):
        result.append(left_data[i])
        i += 1

    while j < len(right_data):
        result.append(right_data[j])
        j += 1

    return result

n = int(input())
data = [0] * n
for i in range(n):
    data[i] = int(input())

for i in split(data):
    print(i)




