Дней на выполнение: 7

result: 30/100

1) **Сильные стороны**
- Использован модуль `abc` и декоратор `@abstractmethod`, что соответствует требованию создания абстрактного класса.
- В классе `PercentDiscount` в методе `__init__` корректно используется `super().__init__(name)`.
- В методе `apply` класса `PercentDiscount` предпринята попытка использовать `super().clamp_price(price)` для нормализации цены, что соответствует требованию.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- Код неполный: отсутствуют классы `FixedDiscount`, `PriceCalculator` и `MinPriceDiscount`, а также блок проверки в конце программы. Это нарушает основные требования задания.
- В классе `DiscountPolicy` метод `__init__` содержит `return self.name`, что некорректно для конструктора (__init__ не должен возвращать значение). Это может вызвать ошибку при создании экземпляра.
- В классе `DiscountPolicy` абстрактный метод `apply` имеет реализацию (присваивает `self.price` и возвращает его), что противоречит концепции абстрактного метода. Он должен быть объявлен без реализации.
- В классе `PercentDiscount` в методе `apply` используется переменная `normalized_price`, но ранее определена переменная `normal_price`. Это приведёт к ошибке `NameError`.
- В конце файла есть лишний символ `К` и пустая строка, что может вызвать синтаксическую ошибку.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- В классе `DiscountPolicy` параметр `name` в `__init__` имеет аннотацию `"Base"` (строка), а не тип `str`. Это не ошибка выполнения, но нарушает общепринятые практики аннотаций типов.
- В методе `apply` класса `PercentDiscount` не выполняется проверка, что `self.percent` может быть не числом или выходить за разумные пределы (например, отрицательный процент). Хотя это явно не требуется, это может привести к неожиданным результатам.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- Имя переменной `discoun_price` содержит опечатку (пропущена буква 't').
- В методе `apply` класса `PercentDiscount` отсутствует docstring или комментарии, объясняющие логику.
- Отступы и форматирование не везде consistent (например, пробелы вокруг операторов).

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 15/50 (минус 35 за отсутствие большей части требуемых классов и блокирующие ошибки в существующем коде)
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 10/30 (минус 20 за некорректный абстрактный метод, ошибку в конструкторе, незавершённость и опечатки)
- Стиль и тесты: 5/20 (минус 15 за отсутствие тестового блока и стилевые недочёты)

Итог: 30/100

4) **Если задание выполнено не полностью**
- Отсутствует класс `FixedDiscount`.
- Отсутствует класс `PriceCalculator`.
- Отсутствует класс `MinPriceDiscount` (задача 2).
- Отсутствует блок проверки в конце программы.
- Существующий код содержит синтаксические и логические ошибки.

**Вариант полного решения (краткий код):**

```python
from abc import ABC, abstractmethod

class DiscountPolicy(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply(self, price: float) -> float:
        pass

    def clamp_price(self, price: float) -> float:
        return max(0.0, price)

class PercentDiscount(DiscountPolicy):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        return normalized_price * (1 - self.percent / 100)

class FixedDiscount(DiscountPolicy):
    def __init__(self, name: str, amount: float):
        super().__init__(name)
        self.amount = amount

    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        return max(0.0, normalized_price - self.amount)

class MinPriceDiscount(DiscountPolicy):
    def __init__(self, name: str, min_price: float, percent: float):
        super().__init__(name)
        self.min_price = min_price
        self.percent = percent

    def apply(self, price: float) -> float:
        normalized_price = super().clamp_price(price)
        if normalized_price < self.min_price:
            return normalized_price
        return normalized_price * (1 - self.percent / 100)

class PriceCalculator:
    def __init__(self, policies: list[DiscountPolicy]):
        self.policies = policies

    def calculate(self, price: float) -> float:
        result = price
        for policy in self.policies:
            result = policy.apply(result)
        return result

if __name__ == "__main__":
    percent_policy = PercentDiscount("10% off", 10)
    fixed_policy = FixedDiscount("250 off", 250)
    min_price_policy = MinPriceDiscount("5% above 1000", 1000, 5)

    calculator = PriceCalculator([percent_policy, fixed_policy, min_price_policy])

    print(calculator.calculate(1500))
    print(calculator.calculate(500))
```
