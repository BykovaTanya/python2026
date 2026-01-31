
# -*- coding: utf-8 -*-

"""
Пример операций со множествами в Python
"""

# Создание множеств
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8}
set_c = {1, 2, 3}

print(f"Множество A: {set_a}")
print(f"Множество B: {set_b}")
print(f"Множество C: {set_c}")

# 1. Объединение (union) - все элементы из обоих множеств
union_ab = set_a | set_b  # или set_a.union(set_b)
print(f"\nОбъединение A ∪ B: {union_ab}")

# 2. Пересечение (intersection) - общие элементы
intersection_ab = set_a & set_b  # или set_a.intersection(set_b)
print(f"Пересечение A ∩ B: {intersection_ab}")

# 3. Разность (difference) - элементы из A, которых нет в B
difference_ab = set_a - set_b  # или set_a.difference(set_b)
print(f"Разность A \\ B: {difference_ab}")

# 4. Симметрическая разность (symmetric difference) - элементы из одного множества, но не из обоих
sym_diff_ab = set_a ^ set_b  # или set_a.symmetric_difference(set_b)
print(f"Симметрическая разность A Δ B: {sym_diff_ab}")

# 5. Проверка подмножества
is_subset = set_c <= set_a  # или set_c.issubset(set_a)
print(f"\nC является подмножеством A: {is_subset}")

# 6. Проверка надмножества
is_superset = set_a >= set_c  # или set_a.issuperset(set_c)
print(f"A является надмножеством C: {is_superset}")

# 7. Проверка пересечения
has_intersection = set_a.isdisjoint({9, 10})
print(f"A не пересекается с {{9, 10}}: {has_intersection}")

# 8. Добавление и удаление элементов
set_d = {1, 2, 3}
set_d.add(4)  # добавить элемент
print(f"\nПосле добавления 4: {set_d}")

set_d.update({5, 6})  # добавить несколько элементов
print(f"После добавления 5, 6: {set_d}")

set_d.remove(1)  # удалить элемент (вызовет ошибку, если элемента нет)
print(f"После удаления 1: {set_d}")

set_d.discard(10)  # удалить элемент (без ошибки, если элемента нет)
print(f"После попытки удаления 10: {set_d}")

# 9. Популярное использование: удаление дубликатов из списка
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5, 5]
numbers = list(set(numbers_with_duplicates)) # Удаление дубликатов

# 10. Генератор множества
squares = {x**2 for x in range(5)}
print(f"\nКвадраты чисел 0-4: {squares}")

# 11. Проверка принадлежности
print(f"\n2 в set_a: {2 in set_a}")
print(f"10 в set_a: {10 in set_a}")
