#  better version using the constructor
def show(self):
        print("Student Roll Number:", self.roll_number)
        print("Student Name:", self.name)
class Student:
    def __init__(self, roll: int, name: str):
# validation of the type 
        if not isinstance(roll, int):
            raise TypeError("Roll number must be an integer")

        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        self.roll_number = roll
        self.name = name

    def display(self):
        print("Student Roll Number:", self.roll_number)
        print("Student Name:", self.name)
# correct usage of passing the data to the specific datatype of the variable
s = Student( roll ="Rohit",name=223)
s.display()