sections = input().split('-') # -를 기준으로 괄호를 치면된다.
# -를 기준으로 영역을 나누어 합한 후, 그 값들을 차례대로 빼주면된다.

numbers = []
for plus_section in sections:
    opponent = map(int, plus_section.split('+'))
    numbers.append(sum(opponent))

result = numbers[0]
for i in range(1, len(numbers)):
    result -= numbers[i]
print(result)