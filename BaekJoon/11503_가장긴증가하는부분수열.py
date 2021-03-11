n = int(input())
numbers = list(set(map(int, input().split())))
sequences = dict()

sequences[numbers[0]] = 1

for number in numbers[1:]:
    value = 0
    for key, length in sequences.items():
        if key < number:
            value = max(value, length)
        else:
            sequences[key] += 1
    sequences[number] = value + 1

print(sequences[max(numbers)])
