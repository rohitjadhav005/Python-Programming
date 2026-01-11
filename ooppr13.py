class Dog:
    species1 = "labroder" # Class attribute
    species2 = "german shepard" # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
# Creating an object of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Tommy", 4 )
print(dog1.name) 
print(dog1.age)
print(dog1.species1)
print(dog2.name) 
print(dog2.age)
print(dog2.species2)