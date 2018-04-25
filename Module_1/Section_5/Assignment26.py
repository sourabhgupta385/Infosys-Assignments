'''
@author: SOURABH GUPTA
'''
'''
Consider a scenario from ABC Training Institute.
Given below are two Sets representing the names of students enrolled for a particular course:
java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}
Write a Python program to list the number of students enrolled for:
1)Python course
2)Java course only
3)Python course only
4)Both Java and Python courses
5)Either Java or Python courses but not both
6)Either Java or Python courses
'''
java_course = {"John", "Jack", "Jill", "Joe"}
python_course = {"Jake", "John", "Eric", "Jill"}

print("Numer of student enrolled in python : ",python_course.__len__())
print("Numer of student enrolled in java only : ",(java_course - python_course).__len__())
print("Numer of student enrolled in python only : ",(python_course - java_course).__len__())
print("Numer of student enrolled in java & python : ",(java_course & python_course).__len__())
print("Numer of student enrolled in java or python : ",(java_course | python_course).__len__())
print("Numer of student enrolled in either java or python but not both : ",(java_course ^ python_course).__len__())
