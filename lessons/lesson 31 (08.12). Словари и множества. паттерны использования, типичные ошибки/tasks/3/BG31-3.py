set_a = {'leo', 'sveta', 'arina'}
set_b = {'leo', 'irina', 'mark'}
both = set_a & set_b
print("Посетил оба спектакля: ",both)
set_b = list(set_b)
print(set_b)
free = set_b[1:]
set_b = set(free)
print("Свободны для распределения: ",set_b)
