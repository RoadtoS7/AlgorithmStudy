numbers = input()

one_count = 0
zero_count = 0

if numbers[0] == '0':
    one_count += 1
if numbers[0] == '1':
    zero_count += 1

for i in range(len(numbers) - 1):
    if numbers[i] != numbers[i + 1]:
        if numbers[i + 1] == '1':
            zero_count += 1
        if numbers[i + 1] == '0':
            one_count += 1



print(min(zero_count, one_count))

