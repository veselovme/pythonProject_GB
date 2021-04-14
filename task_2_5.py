price = [12.2, 45, 45.6, 67.55, 76.12, 45.65, 56.6, 87, 54.56, 43,4]
price_new = []

for i in price:
    i = int(round(i * 100))
    r = i // 100
    kk = i % 100
    price_new.append(f"{r} руб {kk:02d} коп")
print(", ".join(price_new))

id1 = id(price)
price.sort()
print(price)
print(id(price))
print(id1)

price_new = sorted(price, reverse=True)
print(price_new)
print(sorted(price_new[:5]))