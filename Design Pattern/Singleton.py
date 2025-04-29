#singleton design pattern says  there should be only one instance for a particular class

class Singelton():
    __instance = None

    @staticmethod
    def get_instance():
        if Singelton.__instance == None:
            Singelton()

        return Singelton.__instance
    
    def __init__(self):
        if Singelton.__instance != None:
            raise Exception("Direct object cant be created please use get_instance method to  get a instance")
        else:
            Singelton.__instance = self
obj = Singelton()
print(obj)
obj1 = Singelton.get_instance()
obj2 = Singelton.get_instance()
print("obj1",obj1)
print("obj2",obj2)