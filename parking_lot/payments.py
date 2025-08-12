from abc import ABC , abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
       pass

class CardPayment(Payment):

    def pay(self,amount):
        print(f"{amount}$ paid.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"{amount}$ paid.")
        