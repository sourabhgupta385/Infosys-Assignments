'''
@author: SOURABH GUPTA
'''
'''
Consider a ﬁle 'courses.txt' with the following details:
Java
Python
Javascript
PHP
Write a program to read the ﬁle and store the courses in Python variables as a:
1)Dictionary ( Sample - {0: 'Java', 1: 'Python', 2:'Javascript' 3: 'PHP'} )
2)List ( Sample - ['Java', 'Python', 'Javascript', 'PHP'] )
'''
result = open("course.txt","r")
lines = result.readlines()
course_dict = {}
course_list = [None] * len(lines)
i = 0
for line in lines:
    course_dict[i] = line.split()
    course_list[i] = line.split()
    i = i + 1
print(course_dict)
print(course_list)
