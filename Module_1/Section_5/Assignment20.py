'''
Created on 25-Mar-2018

@author: SOURABH GUPTA
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