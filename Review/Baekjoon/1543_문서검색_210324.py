document, word = input(), input()

i, result = 0, 0
while len(document) - i >= len(word):
    if document[i: i + len(word)] == word:
        result += 1
        i += len(word)
    else:
        i += 1

print(result)
