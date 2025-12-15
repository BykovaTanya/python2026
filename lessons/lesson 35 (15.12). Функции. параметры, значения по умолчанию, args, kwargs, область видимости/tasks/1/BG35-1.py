def calculate_order (price_per_item,quantity,discount):
    total = float(price_per_item * quantity)
    return total
    result = float(total * (1 - discount / 100))
    return result
print(calculate_order(100,3,10))
