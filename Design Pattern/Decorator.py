# What it does:
# Decorator allows you to add new behavior to objects without modifying their structure or code.
# Real-world analogy:
# Think of a plain coffee .
# You can add milk, add sugar, add whipped cream, etc. — but the original coffee remains unchanged.


class Coffee:
    def cost(self):
        return 40
    
class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()+10
    
class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee
        
    def cost(self):
        return self.coffee.cost()+30
    

my_coffee = Coffee()
my_coffee = SugarDecorator(my_coffee)
my_coffee = MilkDecorator(my_coffee)


print(my_coffee.cost())