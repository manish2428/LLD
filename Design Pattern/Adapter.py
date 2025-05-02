# You have a class that doesn't match the interface you need, but you still want to use it — without modifying it.
# Example Scenario:
# You’re writing a drawing program that expects objects with a draw() method.
# But you have an old library that uses a render() method instead.

class BankService:
    def make_payment(self, amount):
        print(f"{amount}$ has been processed from your bank account")

class PaymentService:
    def pay(self, amount):
        pass
        
class PaymentAdapter(PaymentService):
    def __init__(self, service : BankService):
        self.service = service

    def pay(self, amount):
        self.service.make_payment(amount)

bank_service = BankService()
payment = PaymentAdapter(bank_service)
payment.pay(100)   
