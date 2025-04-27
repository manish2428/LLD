# L => Liscove Substitution Problem
# ->Child classes should work perfectly when used instead of parent class

#####   BAD EXAMPLE  #####

# class Bird:
#     def fly(self):
#         pass

# class Penguin(Bird):
#     def fly(self):
#         raise Exception("Penguin can't fly")   
# penguin = Penguin()
# penguin.fly()

#penguin is a bird but it voilates the behaviour


# Sparrow is a FlyingBird — it can fly 
# Penguin is just a Bird — it can walk 
# No broken behavior anymore.
# Substituting a Penguin for Bird works fine (only uses walk).
# No surprises. No crash. Full safety.

class Bird:
    def walk(self):
        pass
    
class FlyingBird(Bird):
    def fly(self):
        pass


class Sparrow(FlyingBird):
    def fly(self):
        print(f"{self.__class__.__name__} is flying!!")

class Penguin(Bird):
    def walk(self):
        print(f"{self.__class__.__name__} is walking")

def make_bird_walk(bird : Bird):
    bird.walk()

def make_bird_fly(bird : FlyingBird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
make_bird_walk(sparrow)




# make_bird_walk expects a Bird.
# ✅ Both Sparrow and Penguin behave correctly.

# make_bird_fly expects a FlyingBird.
# ✅ Only Sparrow can fly.
# 🚫 Penguin cannot be passed here (type mismatch)!

# No weird surprises. No exceptions.
# This is what LSP wants.