'''
@author: SOURABH GUPTA
'''
'''
Write a Python program to generate ﬁrst 'n' Fibonacci numbers where 'n' is accepted as an input from the user. 
Store the generated Fibonacci numbers in a list and display the output.
Sample input: 5
Sample output: [0, 1, 1, 2, 3]
'''
num1 = 0
num2 = 1
num3 = []
num3.append(num1)
num3.append(num2)
n = int(input("Input a number"))
for i in range(2,n):
    num3.append(num1 + num2)
    num1 = num2
    num2 = num3[-1]

print(num3)
