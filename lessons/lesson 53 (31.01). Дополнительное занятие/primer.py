#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пример кода, содержащий все базовые элементы синтаксиса Python
"""

# 1. Переменные и базовые типы данных
integer_var = 42  # Целое число
float_var = 3.14  # Число с плавающей точкой
string_var = "Привет, мир!"  # Строка
boolean_var = True  # Булево значение
none_var = None  # Отсутствие значения

# 2. Списки (list)
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "два", 3.0, True, None]
nested_list = [[1, 2], [3, 4], [5, 6]]

# 3. Кортежи (tuple) - неизменяемые списки
coordinates = (10, 20)
rgb = (255, 128, 0)

# 4. Словари (dict) - ключ-значение
person = {
    "имя": "Иван",
    "возраст": 25,
    "город": "Москва",
    "хобби": ["программирование", "чтение", "спорт"]
}

# 5. Множества (set) - уникальные элементы
unique_numbers = {1, 2, 3, 4, 5}
letters = set("абвгд")
# | - объединение, & - пересечение, - - разность, ^ - симметрическая разность

# 6. Условные конструкции
def check_number(num):
    """Проверяет число и возвращает описание"""
    if num > 0:
        return "Положительное"
    elif num < 0:
        return "Отрицательное"
    else:
        return "Ноль"

# 7. Циклы
# Цикл for
def print_numbers(limit):
    """Выводит числа от 0 до limit"""
    for i in range(limit):
        if i % 2 == 0:
            print(f"{i} - четное")
        else:
            print(f"{i} - нечетное")

# Цикл while
def countdown(count):
    """Обратный отсчет"""
    while count > 0:
        print(count)
        count -= 1
    print("Пуск!")

# 8. Функции
def add_numbers(a, b):
    """Складывает два числа"""
    return a + b

def greet(name="гость"):
    """Приветствие с параметром по умолчанию"""
    return f"Здравствуйте, {name}!"

# Функция с переменным числом аргументов
def sum_all(*args):
    """Суммирует все переданные числа"""
    total = 0
    for num in args:
        total += num
    return total

# Функция с именованными аргументами
def create_profile(**kwargs):
    """Создает профиль пользователя"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

# 9. Генераторы списков
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]

# 10. Лямбда-функции
multiply = lambda x, y: x * y
is_even = lambda x: x % 2 == 0

# 11. Классы и объекты
class Animal:
    """Базовый класс животного"""
    
    # Атрибут класса
    species = "неизвестно"
    
    def __init__(self, name, age):
        """Конструктор"""
        self.name = name
        self.age = age
    
    def make_sound(self):
        """Издает звук"""
        return "Какой-то звук"
    
    def info(self):
        """Информация о животном"""
        return f"{self.name}, {self.age} лет, вид: {self.species}"

class Dog(Animal):
    """Дочерний класс - Собака"""
    
    # Переопределение атрибута класса
    species = "собака"
    
    def __init__(self, name, age, breed):
        """Конструктор с дополнительным параметром"""
        super().__init__(name, age)  # Вызов конструктора родителя
        self.breed = breed
    
    # Переопределение метода
    def make_sound(self):
        return "Гав-гав!"
    
    # Новый метод
    def wag_tail(self):
        return f"{self.name} виляет хвостом"

# 12. Исключения
def divide(a, b):
    """Деление с обработкой исключений"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: неверный тип данных!")
        return None
    finally:
        print("Попытка деления завершена")

# 13. Работа с файлами
def write_to_file(filename, content):
    """Записывает содержимое в файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Файл {filename} успешно записан")
    except IOError as e:
        print(f"Ошибка записи в файл: {e}")

def read_from_file(filename):
    """Читает содержимое из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except IOError as e:
        print(f"Ошибка чтения файла: {e}")
        return None

# 14. Модули и импорты
import math  # Стандартный модуль
from datetime import datetime  # Импорт конкретного класса

# 15. Декораторы
def timing_decorator(func):
    """Декоратор для измерения времени выполнения"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция {func.__name__} выполнилась за {end - start:.4f} секунд")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """Пример функции с декоратором"""
    import time
    time.sleep(0.1)
    return "Готово!"

# 16. Контекстные менеджеры
class CustomContext:
    """Пример контекстного менеджера"""
    
    def __enter__(self):
        print("Вход в контекст")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Выход из контекста")
        return False

# 17. Итераторы
class CountDown:
    """Пример итератора"""
    
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

# 18. Комprehensions для словарей и множеств
dict_comp = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
set_comp = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}

# 19. F-строки (форматированные строки)
name = "Анна"
age = 30
formatted = f"Имя: {name}, Возраст: {age}, Возраст в квадрате: {age**2}"

# 20. Основная часть программы
if __name__ == "__main__":
    # Демонстрация работы кода
    
    print("=== Базовые типы данных ===")
    print(f"Целое: {integer_var}, Тип: {type(integer_var)}")
    print(f"Вещественное: {float_var}, Тип: {type(float_var)}")
    print(f"Строка: {string_var}, Тип: {type(string_var)}")
    print(f"Булево: {boolean_var}, Тип: {type(boolean_var)}")
    print(f"None: {none_var}, Тип: {type(none_var)}")
    
    print("\n=== Работа со списками ===")
    print(f"Список чисел: {numbers}")
    print(f"Первый элемент: {numbers[0]}")
    print(f"Последний элемент: {numbers[-1]}")
    print(f"Срез [1:3]: {numbers[1:3]}")
    numbers.append(6)
    print(f"После добавления 6: {numbers}")
    
    print("\n=== Работа с кортежами ===")
    print(f"Координаты: {coordinates}")
    print(f"X: {coordinates[0]}, Y: {coordinates[1]}")
    
    print("\n=== Работа со словарями ===")
    print(f"Человек: {person}")
    print(f"Имя: {person['имя']}")
    print(f"Возраст: {person['возраст']}")
    person['email'] = "ivan@example.com"
    print(f"После добавления email: {person}")
    
    print("\n=== Работа с множествами ===")
    print(f"Уникальные числа: {unique_numbers}")
    unique_numbers.add(6)
    print(f"После добавления 6: {unique_numbers}")
    
    print("\n=== Условные конструкции ===")
    print(f"Число 5: {check_number(5)}")
    print(f"Число -3: {check_number(-3)}")
    print(f"Число 0: {check_number(0)}")
    
    print("\n=== Циклы ===")
    print("Цикл for:")
    print_numbers(5)
    print("\nЦикл while:")
    countdown(3)
    
    print("\n=== Функции ===")
    print(f"2 + 3 = {add_numbers(2, 3)}")
    print(greet())
    print(greet("Мария"))
    print(f"Сумма 1+2+3+4 = {sum_all(1, 2, 3, 4)}")
    
    profile = create_profile(name="Петр", age=35, city="СПб")
    print(f"Профиль: {profile}")
    
    print("\n=== Генераторы списков ===")
    print(f"Квадраты: {squares}")
    print(f"Четные числа: {even_numbers}")
    
    print("\n=== Лямбда-функции ===")
    print(f"5 * 4 = {multiply(5, 4)}")
    print(f"6 четное? {is_even(6)}")
    
    print("\n=== Классы и объекты ===")
    animal = Animal("Животное", 5)
    print(animal.info())
    print(f"Звук: {animal.make_sound()}")
    
    dog = Dog("Рекс", 3, "Овчарка")
    print(dog.info())
    print(f"Звук: {dog.make_sound()}")
    print(dog.wag_tail())
    
    print("\n=== Исключения ===")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
    
    print("\n=== Работа с файлами ===")
    test_content = "Это тестовый файл\nПривет, мир!"
    write_to_file("test.txt", test_content)
    content = read_from_file("test.txt")
    if content:
        print(f"Содержимое файла: {content.strip()}")
    
    print("\n=== Модули ===")
    print(f"Пи: {math.pi}")
    print(f"Квадратный корень из 16: {math.sqrt(16)}")
    print(f"Текущая дата и время: {datetime.now()}")
    
    print("\n=== Декораторы ===")
    result = slow_function()
    print(f"Результат: {result}")
    
    print("\n=== Контекстные менеджеры ===")
    with CustomContext():
        print("Внутри контекста")
    
    print("\n=== Итераторы ===")
    print("Обратный отсчет с помощью итератора:")
    for num in CountDown(3):
        print(num)
    
    print("\n=== Comprehensions ===")
    print(f"Словарь: {dict_comp}")
    print(f"Множество: {set_comp}")
    
    print("\n=== F-строки ===")
    print(formatted)
    
    print("\n=== Программа завершена ===")