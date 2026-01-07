age = -1
while age < 0:
        age = float(input("Enter your age: "))
        if age < 0:
            print("Invalid age. Please enter a positive number.")
            print("Age:", age)
        else:
              print("Valid age is entered:", age)