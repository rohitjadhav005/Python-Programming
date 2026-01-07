def sum(n):
    if n<10:
        return n
    else:
        return n % 10 + sum(n//10)       
num = 464810
result = sum(num)
print(f"The sum of the digits of {num} is {result}")