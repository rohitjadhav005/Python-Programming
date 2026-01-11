#In this programm we are learning the concept of the inheritance in python
#Here the Class Employee is the Father of the Class Programmer
#we can call the Employee class indirectly by using the child class which is give beloww is nothing but the Programmer
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the employee is {self.name} & The ID of the employee is {self.id}.")
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is python")
Emp1 = Programmer("Rohit",1234)
Emp1.showDetails()
Emp1.showLanguage()

Emp2 = Programmer("Himanshu",3214)
Emp2.showDetails()
Emp2.showLanguage()
 