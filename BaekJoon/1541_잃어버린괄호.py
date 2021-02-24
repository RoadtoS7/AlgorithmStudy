math_expression = input()
start, end = 0, 1

result = 0
candidate = 0
isMinusExist = False
while start < len(math_expression) and end < len(math_expression):
    if math_expression[end].isnumeric():
        end += 1
        continue

    if math_expression[end] == '+':
        number = int(math_expression[start: end])
        candidate += number
        end += 1
        start = end
        continue

    if math_expression[end] == '-':
        number = int(math_expression[start: end])
        candidate += number
        if isMinusExist:
            result -= candidate
        else:
            result += candidate
        isMinusExist = True
        candidate = 0
        end += 1
        start = end
        continue

number = int(math_expression[start: end])
candidate += number
if start != 0 and isMinusExist:
    result -= candidate
else:
    result += candidate

print(result)