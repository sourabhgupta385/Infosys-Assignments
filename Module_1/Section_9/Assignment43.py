'''
@author: SOURABH GUPTA
'''
'''
The ABC Institute oﬀers vocational courses to students in multiple areas
e.g. theatre, classical singing, traditional dance forms, Bollywood dance, literature and so on. 
A student can enroll for zero to all courses.
Write a Python function that takes the number of courses as an input and
returns the total number of diﬀerent course combinations, a student can opt for.
(Make use of functions available in math module)
'''
import math
import time
def combinations():
    no_of_courses = int(input("Enter the number of courses"))
    course_combination = math.factorial(no_of_courses)
    return course_combination

print("Number of course combination possible : ", combinations())
