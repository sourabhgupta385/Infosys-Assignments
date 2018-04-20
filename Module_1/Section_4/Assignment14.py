'''
@author: SOURABH GUPTA
'''
'''
a. Display all even numbers between 50 and 80 (both inclusive) using "for" loop.
b. Add natural numbers up to n where n is taken as an input from user. Print the sum.
c. Prompt the user to enter a number. Print whether the number is prime or not.
d. Print Fibonacci series till nth term where n is taken as an input from user.
Hint – Fibonacci series is a series of numbers in which each number is the sum of the two precedingnumbers.
Series start from 1 and goes like : 1, 1, 2, 3, 5, 8, 13 … .
'''
#even numbers
from builtins import range

for i in range(50,81):
    if i%2 == 0:
        print(i)

#add natural numbers
n = input("Input a number")
n = int(n)
sum = 0
for i in range(1,n+1):
    sum = sum + i
print("Sum is : ",sum)

#prime number
n = input("Input a number")
n = int(n)
flag = 0
for i in range(2,int(n/2)+1):
    if n % i == 0:
        flag = 1
        break
if flag == 1:
    print("Not Prime")
else:
    print("Prime")

#print fibonacci
n1 = 1
n2 = 1
n = input("Input a number")
n = int(n)
print(n1)
print(n2)
for i in range(1,n+1):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
