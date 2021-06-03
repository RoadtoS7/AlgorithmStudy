T = int(input())

# sentences = []
# for _ in range(T):
#     reversed_input = map(reversed, input().split())
#     sentence = map(list, reversed_input)
#     sentences.append(sentence)
#
# for sentence in sentences:
#     for word in sentence:
#         print("".join(word), end=" ")
#     print()
#
#
# T = int(input())

sentences = [input().split() for _ in range(T)]

for sentence in sentences:
    for word in sentence:
        print("".join(list(reversed(word))), end=" ")
    print()








