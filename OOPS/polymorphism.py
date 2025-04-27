from abc import ABC, abstractmethod

class PaymentMethod:

    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}$ paid through CreditCard")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}$ paid through PayPal")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"{amount}$ paid through UPI")

def pay(paymentmethod : PaymentMethod, amount):
    paymentmethod.pay(amount)

creditcard = CreditCard()
paypal = PayPal()
upi = UPI()

pay(creditcard, 2000)
pay(paypal, 2000)
pay(upi, 2000)
pay(UPI(), 8000)


'''
- All classes share the same method name pay().
- Each one implements it differently.
- You can interchange them without changing the process_payment() function.



#Real-World Benefits:
- Add a new payment type (e.g., UPI) without touching existing code.

- Reduces if-else blocks or type-checking.

- Easy to extend, test, and maintain.

'''