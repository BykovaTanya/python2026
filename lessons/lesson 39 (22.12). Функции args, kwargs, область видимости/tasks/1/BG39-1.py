
def existing_scores(*values):
    if not values:
        raise ValueError("Введите хотя бы один балл")
    avg = sum(values)/len(values)
    deviations = abs(values) 
    
    list = []
    for val in values:
        list.append(round(total_values/length, 1))
    return tuple(list)


existing_scores = [10, 8, 6]
print(mean_abs_deviation(*existing_scores))



