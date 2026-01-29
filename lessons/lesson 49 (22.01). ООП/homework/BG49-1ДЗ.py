from abc import ABC, abstractmethod
class  DiscountPolicy(ABC):
    def __init__(self, name: "Base"):
        self.name = name
        return self.name

    @abstractmethod
    def apply(self, price: float):
        self.price = price
        return self.price

    def clamp_price(self, price: float):
        if price < 0:
            return 0
        else:
            return price

class PercentDiscount(DiscountPolicy):
    def __init__(self, name, percent):
        super().__init__(name) 
        self.percent = percent

    def apply(self, price):
        normal_price = super().clamp_price(price)
        discoun_price = normalized_price * (1 - self.percent/100) 
    return discoun_price

К
    