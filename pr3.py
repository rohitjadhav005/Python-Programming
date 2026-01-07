# take user input of a number and check whether the no is even or odd 
num  = int(input("Enter a Number:"))
if num %2 ==0:
    print(f"{num} is Even Number")
elif num %2 !=0:
    print(f"{num} is Odd Number")
else:
    print("Invalid Input OR Number is Zero!")