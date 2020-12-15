from collections import defaultdict

book = defaultdict(int)

n = int(input())

for _ in range(n):
    book_name = input()
    book[book_name] += 1

bestseller = sorted(list(book.items()), key=lambda x: x[1], reverse=True)
top_seller = list()
for item in bestseller:
    if item[1] == bestseller[0][1]:
        top_seller.append(item)

top_seller = sorted(top_seller)
print(top_seller[0][0])


