'''
@author: SOURABH GUPTA
'''
'''
Consider the pseudo code for generating Fibonacci series using Recursion:FIBO (number) 
1. if (number = 0) then
2. return (0)
3. else if (number = 1) then
4. return (1)
5. else
6. return FIBO(number - 1) + FIBO(number - 2)
7. end if
Write a program in Python to implement the same using Recursion and execute it in Eclipse.
Print appropriate error message if the user enters negative number as input.
'''
def FIBO(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return FIBO(number - 1) + FIBO(number - 2)

number = int(input("Enter a number"))
if number > 0:
    for i in range(0,number):
        print(FIBO(i),end = " ")
else:
    print("Invalid input...Enter a positive number")
