A, B, C = int(input()), int(input()), int(input())

result = str(A * B * C)
count = {str(i): 0 for i in range(10)}

for letter in result:
    count[letter] += 1

for value in count.values():
    print(value)
