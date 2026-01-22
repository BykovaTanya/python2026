Время затраченное на выполнение: 0:22

result: 10/100

1) **Сильные стороны**
- Студент попытался использовать абстрактный класс и наследование, что соответствует теме задания.
- В коде есть попытка определить абстрактный метод `send` и метод `format_message`.

2) **Ошибки и недочёты**

**Блокирующие (ломает выполнение требований задания)**
- Класс `NotificationChannel` некорректно реализован:
  - Атрибут `sender_name` определён как атрибут класса, а не как параметр, который должен храниться в экземпляре. По условию, `sender_name` должен храниться в классе (видимо, как атрибут экземпляра, инициализируемый в `__init__`, но в условии явно не указан `__init__` для абстрактного класса, поэтому его можно не добавлять, но тогда `sender_name` должен быть передан в `__init__` наследников). В текущей реализации `sender_name` — это атрибут класса со значением `"MyService"`, что не позволяет задавать разные имена отправителей для разных каналов, как требуется (например, `EmailChannel` должен принимать `sender_name` в `__init__`).
  - Метод `format_message` определён как обычный метод, но не принимает параметр `self`, поэтому не может обращаться к `self.sender_name`. Вместо этого он пытается использовать переменную `sender_name`, которая не определена в области видимости метода, что вызовет ошибку `NameError`.
  - После определения класса есть вызовы `format_message = format_message()` и `print(format_message())`, которые не имеют смысла и приведут к ошибкам, так как `format_message` — это метод, а не функция.
- Классы `EmailChannel` и `SMSChannel` не реализованы:
  - В `EmailChannel` метод `__init__` не завершён: после заголовка метода нет тела (отсутствует отступ для кода), а строки `super().format_message(message)` и `super().send()` написаны без отступа, что является синтаксической ошибкой. Также `super().send()` вызовет ошибку, так как `send` — абстрактный метод без реализации.
  - В `SMSChannel` метод `__init__` также не имеет тела.
  - Не переопределены методы `send` в наследниках, как требуется по условию.
- Класс `NotificationService` отсутствует полностью.
- Демонстрация работы (создание каналов, сервиса, вызов `notify_all`) отсутствует.
- Код содержит синтаксические ошибки (например, незакрытая строка в `print(f"отправку email)`), что предотвратит запуск.

**Значимые (может дать неверный результат на части кейсов, сильно ухудшает качество)**
- Не используется `super()` в методах `send` наследников для вызова `format_message`, как требуется.
- Нет полиморфизма через `NotificationService`, так как класс не реализован.

**Минорные (стиль, читаемость, мелкие улучшения без влияния на правильность)**
- Имена файлов и пути в комментарии избыточны, но не влияют на выполнение.
- Отсутствуют аннотации типов (не требуется по условию, но улучшило бы читаемость).

3) **Оценка и как она посчитана**
- Функциональность и соответствие условию: 5/50 (реализованы только зачатки абстрактного класса, но с критическими ошибками; наследники и сервис отсутствуют; демонстрации нет).
- Качество кода (структура, читаемость, устойчивость, отсутствие дублирования): 3/30 (код нерабочий, содержит синтаксические ошибки, плохо структурирован).
- Стиль и тесты: 2/20 (тесты не требуются, но код не соответствует PEP 8 в части отступов и оформления; есть явные стилевые недочёты, например, незакрытые строки).
- Итог: 10/100 (округлено от 10).

4) **Если задание выполнено не полностью**
- Отсутствует: корректная реализация абстрактного класса `NotificationChannel`, классы `EmailChannel` и `SMSChannel` с методами `send`, класс `NotificationService`, демонстрация работы.
- Сделано частично: попытка создать абстрактный класс, но с ошибками, которые делают его непригодным.

**Вариант полного решения (код):**

```python
from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    def __init__(self, sender_name: str):
        self.sender_name = sender_name

    def format_message(self, message: str) -> str:
        return f"[{self.sender_name}] {message}"

    @abstractmethod
    def send(self, recipient: str, message: str) -> None:
        pass

class EmailChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_email: str):
        super().__init__(sender_name)
        self.sender_email = sender_email

    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"EMAIL to {recipient}: {formatted_message} (from {self.sender_email})")

class SMSChannel(NotificationChannel):
    def __init__(self, sender_name: str, sender_phone: str):
        super().__init__(sender_name)
        self.sender_phone = sender_phone

    def send(self, recipient: str, message: str) -> None:
        formatted_message = super().format_message(message)
        print(f"SMS to {recipient}: {formatted_message} (from {self.sender_phone})")

class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels

    def notify_all(self, recipient: str, message: str) -> None:
        for channel in self.channels:
            channel.send(recipient, message)

# Демонстрация работы
if __name__ == "__main__":
    email_channel = EmailChannel("MyService", "noreply@example.com")
    sms_channel = SMSChannel("MyService", "+1234567890")
    service = NotificationService([email_channel, sms_channel])
    service.notify_all("user@example.com", "Hello via email and SMS!")
    service.notify_all("+0987654321", "Another notification")
```
