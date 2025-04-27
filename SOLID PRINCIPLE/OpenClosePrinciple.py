#Open for extension, closed for modification

#bad example

# class Payment:
#     def pay(self, payment_method):
#         if payment_method == "credit_card":
#             print("Payed through credit card")

#         elif payment_method == "debit_card":
#             print("payed through debit card")
# start_payment = Payment()
# start_payment.pay("credit_card")


#Now the problem in above code is if we want to add new payment method here (for eg: "pay_pal") ,we need to change class or modify a class which is kind of risky.
#the class might have been tested before and if you change it then we again have to test it and the class might be dependent to other class or methods so that might through an error.
#so class should be open for extension and closed for modification

#how to fix it
from abc import ABC,abstractmethod
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    
    def pay(self):
        print("Paid through CreditCard")

class DebitCard(Payment):
    
    def pay(self):
        print("Paid through DebitCard")


class PayPal(Payment):
    
    def pay(self):
        print("Paid through PayPal")


def start_payment(payment_type : Payment):
    payment_type.pay()

creditcard = CreditCard()
start_payment(creditcard)

paypal = PayPal()
start_payment(paypal)

debitcard = DebitCard()
start_payment(debitcard)


