document, word = input(), input()
index, result = 0, 0

while len(document) - index >= len(word):
    if document[index:index + len(word)] == word:
        result += 1
        index += len(word)
    else:
        index += 1
print(result)