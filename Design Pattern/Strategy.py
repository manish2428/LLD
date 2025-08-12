from abc import ABC, abstractmethod
class ProcessPayment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(ProcessPayment):
    def pay(self, amount):
        print(f"{amount}$ paid through PayPal")

class UPI(ProcessPayment):
    def pay(self, amount):
        print(f"{amount}$ paid through UPI")


class BitCoin(ProcessPayment):
    def pay(self, amount):
        print(f"{amount}$ paid through BitCoin")

class PaymentStrategy:
    def __init__(self, strategy:ProcessPayment):
        self.strategy = strategy
    
    def set_strategy(self,strategy:ProcessPayment):
        self.strategy = strategy
    
    def process_payment(self, amount):
        self.strategy.pay(amount)


def main():
    amount = 100
    strategy = PaymentStrategy(BitCoin())
    strategy.process_payment(amount)

if __name__ == "__main__":
    main()