from string import ascii_lowercase

word = input()
alphabet_dict = {alphabet:-1 for alphabet in ascii_lowercase}
for i, w in enumerate(word):
    if alphabet_dict[w] == -1:
        alphabet_dict[w] = i

[print(i, end=' ') for i in alphabet_dict.values()]



