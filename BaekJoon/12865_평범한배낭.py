n, k = map(int, input().split())

product = []

for i in range(n):
    w, v = map(int, input().split())
    for item in product:
        if item[1] + w <= k:
            product.append((item[0] + v, item[1] + w))
    product.append((v, w))

print(sorted(product, reverse=True)[0][0])
