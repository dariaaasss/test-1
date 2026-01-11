from abc import ABC, abstractmethod
from typing import List


# Интерфейс стратегии
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# Конкретные стратегии
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}"


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using PayPal ({self.email})"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        return f"Paid ${amount} using Bitcoin ({self.wallet_address[:8]}...)"


# Контекст
class ShoppingCart:
    def __init__(self):
        self.items: List[str] = []
        self.total = 0.0

    def add_item(self, item: str, price: float):
        self.items.append(item)
        self.total += price

    def checkout(self, payment_strategy: PaymentStrategy) -> str:
        result = f"Items: {', '.join(self.items)}\n"
        result += f"Total: ${self.total}\n"
        result += payment_strategy.pay(self.total)
        return result


# Демонстрация
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Laptop", 999.99)
    cart.add_item("Mouse", 29.99)

    print("=== Credit Card Payment ===")
    credit_card = CreditCardPayment("1234567812345678")
    print(cart.checkout(credit_card))

    print("\n=== PayPal Payment ===")
    paypal = PayPalPayment("user@example.com")
    print(cart.checkout(paypal))

    print("\n=== Bitcoin Payment ===")
    bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    print(cart.checkout(bitcoin))