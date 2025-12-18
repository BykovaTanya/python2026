def delivery_price(city, weight_kg, urgent):
    delivery = urgent if 500 + 30 * weight_kg else 300 + 20 * weight_kg
    return delivery

print(delivery_price("moskow",10,urgent=True))
print(delivery_price("ufa",15,urgent=False))
print(delivery_price(city="moskow",weight_kg=10,urgent=True))
print(delivery_price(city="ufa",weight_kg=15,urgent=False))

#print("moskow" + 5)
#print(delivery_price("moskow",10,urgent=True)


