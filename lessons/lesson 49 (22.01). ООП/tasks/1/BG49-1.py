from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    sender_name = "MyService"
    @abstractmethod
    def send(recipient: str, message: str):
        return None
    def format_message(message: str):
        return (f"[{sender_name}] {message}")

format_message = format_message()    
print(format_message())      


class EmailChannel(NotificationChannel):
    def __init__(self,sender_name, sender_email):
    super().format_message(message)
    super().send()
    print(f"отправку email)
class SMSChannel(NotificationChannel):
     def __init__(self,sender_name, sender_phone):


    
        
