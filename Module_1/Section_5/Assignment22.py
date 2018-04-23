'''
Created on 25-Mar-2018

@author: SOURABH GUPTA
'''
courses = ("Python Programming", "RDBMS", "Web Technology", "Software Engg.")
electives = ("Business Intelligence", "Big Data Analytics")

print(courses.__len__())
print(courses)
courses = courses.__add__(electives)
print(courses)