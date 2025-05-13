class Players:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_positon):
        self.position = new_positon
        

