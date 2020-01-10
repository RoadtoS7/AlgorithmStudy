chess = list()

for i in range(8):
    temp = input()
    chess.append(temp)

result = 0

for i in range(0, 7, 2):
    for j in range(i + 1):
        if chess[j][i - j] == 'F':
            result += 1


for i in range(8, 15, 2):
    for j in range(7, i-6):
        if chess[i - j][j] == 'F':
            result += 1

print(result)
