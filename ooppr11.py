# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def show_balance(self):
#         print(self.__balance)
# b = Bank(0)
# # b.__balance = 0  it is dangerus for the 
# b.show_balance()
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