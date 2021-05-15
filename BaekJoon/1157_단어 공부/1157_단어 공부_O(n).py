from collections import defaultdict

word = input()
word_count = defaultdict(int)

for letter in word:
    if letter.islower():
        letter = letter.upper()
    word_count[letter] += 1

max_count = max(word_count.values())
max_result = []
for letter, count in word_count.items():
    if max_count < count:
        max_count = count
        max_result = [letter]
    if max_count == count:
        max_result.append(letter)

if len(max_result) >= 2:
    print('?')
else:
    print(max_result[0])




