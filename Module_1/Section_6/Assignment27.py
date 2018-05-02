'''
@author: SOURABH GUPTA
'''
'''
1. Add natural numbers upto n where n is taken as an input from user.
2. Print Fibonacci series till nth term (Take input from user).
'''
def add_number(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum

def fibonacci(n):
    num1 = 0
    num2 = 1
    num3 = []
    num3.append(num1)
    num3.append(num2)
    for i in range(2,n):
        num3.append(num1 + num2)
        num1 = num2
        num2 = num3[-1]
    return num3

n = int(input("Enter a number"))
print("Sum upto ",n,"is : ",add_number(n))
print("Fibonacci upto ",n,"number is : ",fibonacci(n))
