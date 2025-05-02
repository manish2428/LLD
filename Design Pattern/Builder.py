# #want to build a Burger step by step with optional ingredients like cheese, lettuce, bacon, etc

# class Burger:
#     def __init__(self):
#         self.ingredients = []

#     def add(self, item):
#         self.ingredients.append(item)

#     def show(self):
#         print(f"Your Burger consist of {self.ingredients} ingredients")
    

# class BuildBurger():
#     def __init__(self):
#         self.burger = Burger()

#     def add_buns(self):
#         self.burger.ingredients.append("Bun")
#         return self
    
#     def add_tomatos(self):
#         self.burger.ingredients.append("Sliced Timatos")
#         return self
    
#     def add_onions(self):
#         self.burger.ingredients.append("Sliced Onions")
#         return self
    
#     def add_cheese(self):
#         self.burger.ingredients.append("Cheese")
#         return  self
    
#     def add_wrap(self):
#         self.burger.ingredients.append("Chicken_wrap")
#         return self
    
#     def add_meones(self):
#         self.burger.ingredients.append("Meonese")
#         return self
    
#     def build(self):
#         return self.burger
    
# burger = BuildBurger().add_buns().add_cheese().add_meones().add_onions().add_wrap().build()
# burger.show()


class House:
    def __init__(self, builder):
        self.stories = builder.stories
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type
    
    def show_house(self):
        print(f"Your house contains of {self.stories} stories, {self.door_type} door type and {self.roof_type} roof type")
        return self
    
class BuildHouse():
    def __init__(self):
        self.stories = None
        self.door_type = None
        self.roof_type = None

    def build_stories(self, stories):
        self.stories = stories
        return self
    
    def build_door_type(self, door_type):
        self.door_type = door_type
        return self

    def build_roof_type(self, roof_type):
        self.roof_type = roof_type
        return self
    
    def build_house(self):
        return House(self).show_house()
    
class Contractor:
    def __init__(self, builder):
        self.builder = builder

    def build_one_story_house(self):
        return self.builder().build_stories(1).build_roof_type('Pointy').build_door_type("One").build_house()

    def build_two_story_house(self):    
        return self.builder().build_stories(2).build_roof_type('flat').build_door_type("Two").build_house()

# build_house = BuildHouse()
contractor1 = Contractor(BuildHouse)
one_story_house = contractor1.build_one_story_house()
two_Story_house = contractor1.build_two_story_house()
