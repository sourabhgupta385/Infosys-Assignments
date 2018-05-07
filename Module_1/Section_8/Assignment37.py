'''
@author: SOURABH GUPTA
'''
'''
You have already executed the Python program given below in Functions section:
•Add natural numbers up to n where n is taken as an input from user.

Do appropriate exception handling in the code and observe the output by providing invalid input values.
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
