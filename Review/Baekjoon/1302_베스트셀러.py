n = int(input())

books = {}

for _ in range(n):
    book = input()

    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_value = max(books.values())
array = []
for book, count in books.items():
    if count == max_value:
        array.append(book)

print(sorted(array)[0])




