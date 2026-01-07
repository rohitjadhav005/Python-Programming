def Fib(n):
    if(n==0 or n==1):
        return n
    elif n>1:
        return Fib(n-1)+Fib(n-2)
    else:
        print("Fibonacci numbers begin at 0")
        return
print(Fib(100))