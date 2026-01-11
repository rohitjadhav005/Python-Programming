# learned about the instance and class attibute
class Dog:
    species = "Canine"  # Class attribute
    def __init__(self,speci , name, age):
        self.species = speci
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
    def show(self):
        print("Name of the species: ",self.species)
        print("Name of dog: ",self.name)
        print("age of dog: ",self.age)
d = Dog("Labrador Retriever","juliee",13)
d.show()