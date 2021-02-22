from itertools import permutations

N = int(input())
numbers = input().split()
plus, minus, multiply, divide = map(int, input().split())
min_result = +10000000000
max_result = -10000000000

symbol = []
for _ in range(plus):
    symbol.append('+')

for _ in range(minus):
    symbol.append('-')

for _ in range(multiply):
    symbol.append('*')

for _ in range(divide):
    symbol.append('//')

symbol_set = set(permutations(symbol, N-1))


for symbol in symbol_set:
    result = numbers[0]
    for i in range(1, N):
        if symbol[i-1] == '//' and int(result) < 0:
            result = -eval(("-"+str(result))+symbol[i-1]+numbers[i])
        else:
            result = eval(str(result)+symbol[i-1]+numbers[i])

    if result < min_result:
        min_result = result
    if result > max_result:
        max_result = result

print(max_result, min_result, sep='\n')






