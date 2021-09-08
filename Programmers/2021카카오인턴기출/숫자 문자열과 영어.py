## 3점

def solution(s):
    numbers = [
        ['zero', '0'],
        ['one', '1'],
        ['two', '2'],
        ['three', '3'],
        ['four', '4'],
        ['five', '5'],
        ['six', '6'],
        ['seven', '7'],
        ['eight', '8'],
        ['nine', '9']
    ]

    i = 0
    while i <= 9:
        str, number = numbers[i][0], numbers[i][1]
        index = s.find(str)
        if index >= 0:
            n = len(str)
            s = s[:index] + number + s[index + n:]

        else:
            i += 1

    return int(s)


print(solution("oneone"))
