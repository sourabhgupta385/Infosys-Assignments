'''
Created on 24-Mar-2018

@author: SOURABH GUPTA
'''
'''
Write a Python program for the following requirements:
•Prompt the user to input two numbers num1 and num2
•Increment num1 by 4 and num2 by 6
•Find and print the sum of new values of num1 and num2
'''
num1 = input("Enter number 1")
num2 = input("Enter number 2")
num1 = int(num1)
num2 = int(num2)
num1 = num1 + 4
num2 = num2 + 6
print("Sum of two numbers after incrementing num1 by 4 and num2 by 6 is",num1+num2)
