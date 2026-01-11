class Student:
    roll_number =1
    name = "rohit"
    def show(self):
         print("Student Roll Number: ",self.roll_number)
         print("Student Name: ", self.name)
s= Student()
s.show()
# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def show_balance(self):
#         print(self.__balance)
# b = Bank(0)
# # b.__balance = 0  it is dangerus for the 
# b.show_balance()