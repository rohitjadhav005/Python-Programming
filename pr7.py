# Write a python program to take three numbers from the user and to check the greatest of the three numbers
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
if a>b and a>c:
    print(f"Number {a} is greater than {b} and {c}")
elif b>a and b>c:
    print(f"Number {b} is greater than {a} and {c}")
elif c>a and c>b:
    print(f"Number {c} is greater than {a} and {b}")
else:
    print("All numbers are similar")