class Player:
    def __init__(self, name, symbol):
        self.__name = name
        self.__symbol = symbol

    def get_name(self):
        return self.__name 
    
    def get_symbol(self):
        return self.__symbol