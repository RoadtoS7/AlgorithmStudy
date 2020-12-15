n = int(input())

books = dict()

for _ in range(n):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1


top_selling_count = max(books.values())
best_seller = list()

for book, count in books.items():
    if count == top_selling_count:
        best_seller.append(book)

print(sorted(best_seller)[0])