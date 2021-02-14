import copy

result = []
string = []

def combination(array, length, index):
    if len(string) == length:
        result.append(copy.deepcopy(string))
        return

    for i in range(index, len(array)):
        string.append(array[i])
        combination(array, length, i + 1)
        string.pop()


L, C = map(int, input().split())
vowels = ('a', 'e', 'i', 'o', 'u')

candidates = input().split()
candidates.sort()

combination(candidates, L, 0)

for password in result:
    vowel_count = 0
    for password_char in password:
        if password_char in vowels:
            vowel_count += 1

    if vowel_count >= 1 and vowel_count <= L - 2:
        print(''.join(password))




