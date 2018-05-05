'''
Created on 26-Mar-2018

@author: SOURABH GUPTA
'''
def add_number(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum   
try:
    print(add_number(5))
except TypeError:
    print("INVALID INPUT")
else:
    print("Success")        