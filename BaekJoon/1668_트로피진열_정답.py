def ifAccend(array):
    now = array[0]
    result = 1

    for i in range(1,len(array)):
        if array[i] > now:
            result += 1
            now = array[i]

    return result

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

print(ifAccend(array))
array.reverse()
print(ifAccend(array))

