# write python program to accept a no from user & to calculate given number sum 
num =  int(input("Enter a Number: "))
sum = 0
while num>0:
    rem = num % 10
    sum = sum + rem 
    num =  num//10
print(sum)