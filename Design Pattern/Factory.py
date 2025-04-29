# from abc import ABC,abstractmethod

# class IPeople(ABC):

#     @abstractmethod
#     def peopleRole(self):
#         pass


# class Teacher(IPeople):
#     def peopleRole(self):
#         print(f"class {self.__class__.__name__} is called")

# class Student(IPeople):
#     def peopleRole(self):
#         print(f"class {self.__class__.__name__} is called")

# class PersonFactory:
#     @staticmethod
#     def get_role(people_type):
#         if people_type == "Student":
#             return Student()
        
#         elif people_type == "Teacher":
#             return Teacher()
        
#         else:
#             raise Exception("Invalid people type")
    
# student = PersonFactory.get_role('Student')
# teacher = PersonFactory.get_role('Teacher')
# student.peopleRole()
# teacher.peopleRole()





from abc import ABC,abstractmethod


class Pay(ABC):
    @staticmethod
    def processPayment(self, amount):
        pass

class Paytm(Pay):
    def processPayment(self, amount):
        print(f"{amount} amount has been processed through {self.__class__.__name__}")

class PayPal(Pay):
    def processPayment(self, amount):
        print(f"{amount} amount has been processed through {self.__class__.__name__}")

class CreditCard():
    @staticmethod
    def payment_type(paymentType):
        if paymentType == 'Paytm':
            return Paytm()
        elif paymentType == 'PayPal':
            return PayPal()
        else:
            raise Exception("Invalid Payment Type")
        
payment_type = input("Please enter payment type that you wanna use: ")
amount = input("Please enter the amount: ")

pay = CreditCard.payment_type(paymentType=payment_type)
pay.processPayment(amount=amount)


