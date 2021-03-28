N = int(input())
sales = dict()
for _ in range(N):
    book = input()
    if book in sales:
        sales[book] += 1
    else:
        sales[book] = 1

max_sales = max(sales.values())
best_seller = []
for book, count in sales.items():
    if max_sales == count:
        best_seller.append(book)

print(sorted(best_seller)[0])
