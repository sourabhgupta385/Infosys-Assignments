'''
@author: SOURABH GUPTA
'''
'''
Consider the list of courses opted by a Student "John" and available electives at ABC Training Institute:
courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
electives = ("Business Intelligence", "Big Data Analytics")
Write a Python Program to satisfy business requirements mentioned below:
1.List the number of courses opted by John.
2.List all the courses opted by John.
3.John is also interested in elective courses mentioned above.
Print the updated tuple including electives.
'''
courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
electives = ("Business Intelligence", "Big Data Analytics")

print(courses.__len__())
print(courses)
courses = courses.__add__(electives)
print(courses)
