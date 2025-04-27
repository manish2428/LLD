# "clients should not be forced to depend on interfaces they do not use."
#In simpler terms, ISP suggests that it's better to have multiple, smaller,
# more specific interfaces rather than a large, general-purpose interface that forces clients to implement methods they don't need.

from abc import ABC,abstractmethod
# class MultiFunctionDevice():

#     @abstractmethod
#     def print_document(self):
#         pass

#     @abstractmethod
#     def scan_document(self):
#         pass

# class Printer(MultiFunctionDevice):
    
#     def print_document(self):
#         print("Document is being printed")

#     def scan_document(self):
#         raise Exception("Printer can't scan document")
    
    
# class Scanner(MultiFunctionDevice):
    
#     def print_document(self):
#         raise Exception("Scanner can't print document")

#     def scan_document(self):
#         print("Document is being scanned")
    

# def scan_or_print(device : MultiFunctionDevice):
#     device.scan_document()
#     device.print_document()

# doc = Printer()
# scan_or_print(doc)

#so here in the above code printer doesnt use scan_document feature and scanner doesnt use printe_document function
#but they are forced to use it in the above code which voilated interface segrigation principle because both devices are unnecessarily forced to implement methods they don’t need.


#Now, we split the MultiFunctionDevice into two smaller, more specific interfaces: Printer and Scanner. This allows each device to implement only the methods it needs.


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan_document(Self):
        pass

class LeasurePrinter(Printer):
    def print_document(self):
        print("Document is being printed")

class INCPrinter(Printer):
    def print_document(self):
        print("Document is being printed")
        

class FlatBladeScanner(Scanner):
    def scan_document(Self):
        print("Document is being scanned")

class HandHeldScanner(Scanner):
    def scan_document(Self):
        print("Document is being scanned")


def activate_printer(device:Printer):
    device.print_document()

def activate_scanner(device:Scanner):
    device.scan_document()

doc1 = INCPrinter()
doc2 = HandHeldScanner()
activate_printer(doc1)
activate_scanner(doc2)


###
# In this design:
# The Printer and Scanner interfaces are now separated, so each class only needs to implement the methods relevant to it.
# InkjetPrinter implements Printer, and FlatbedScanner implements Scanner.

# There is no forcing of unnecessary methods to be implemented, and each device class is focused on a specific behavior.
# Summary of Benefits
# Separation of Concerns: The printer and scanner functionalities are separated into distinct interfaces, improving code organization and making it easier to modify or extend.
# Flexibility: You can now add a new device that either prints or scans without affecting the other device's behavior.
# Clean Code: The code is more readable, and each class has only the methods it needs to perform its task.
###