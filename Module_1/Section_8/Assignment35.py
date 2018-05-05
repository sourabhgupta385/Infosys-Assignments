'''
@author: SOURABH GUPTA
'''
'''
Assume the following Python code:
myList = [1,2,3,4,5]
sum = 0
for i in myList:
    sum = sum + i
print(sum)
print(myList[5])

Rewrite the code to handle the exceptions raised.
Print appropriate error messages wherever applicable.

'''
myList = [1,2,3,4,5]
sum = 0

try:
    for i in myList:
        sum = sum + i
    print(sum)
    print(myList[5])
except TypeError:
    print("Please provide integer values")
except IndexError:
    print("Index out of bound")
