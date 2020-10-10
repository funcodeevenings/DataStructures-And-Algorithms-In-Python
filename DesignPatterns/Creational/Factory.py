"""
When a method returns one of several possible classes that share a common super class
    create a new enemy in a game
    random no generator picks a number assigned to a specific enemy
    factory returns enemy associated with that number

The class is chosen at run time
"""

class Dog():
    
    def __init__(self,name):
        self.name=name
        self.sound = "Bhow!"

class Cat():

    def __init__(self,name):
        self.name=name
        self.sound = "Meow!"

def get_pet(pet="dog"):
    '''
    The factory method
    '''
    pets = dict(dog=Dog("Jimi"),cat=Cat("kimi"))
    return pets[pet]

d=get_pet("dog")
c=get_pet("cat")

print(d.sound)
print(c.sound)