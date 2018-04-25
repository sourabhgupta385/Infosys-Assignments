'''
@author: SOURABH GUPTA
'''
'''
Consider a scenario from ABC Training Institute.
The given table shows the marks scored by students of grade XI in Python Programming course.
    Student Name               Marks scored
    John                            86.5
    Jack                            91.2
    Jill                            84.5
    Harry                           72.1
    Joe                             80.5
Write a Python program to meet the requirements mentioned below:
a. Display the name and marks for every student.
b. Display the top two scorers for the course.
c. Display class average of this course.
'''
import operator
result = {"John":86.5, "Jack":91.2, "Jill":84.2, "Harry":72.1, "Joe":80.5}
print(result)
sorted_result = sorted(result.items(), key=operator.itemgetter(1))
print(sorted_result[-1])
print(sorted_result[-2])

sum = 0
for i in result.values():
    sum = sum + i
avg = sum / result.__len__()
print("Avg Marks : ",avg)
