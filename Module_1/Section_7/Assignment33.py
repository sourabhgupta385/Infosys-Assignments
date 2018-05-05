'''
@author: SOURABH GUPTA
'''
'''
Consider a ﬁle 'student_details.txt' with the details of students in ABC institute – student id and name:
101 Rahul
102 Julie
103 Helena
104 Kally
Write a program to read the ﬁle and store the student records in Python variable as:
1)List of lists
2)List of dictionaries
'''
result = open("student_detail.txt","r")
lines = result.readlines()

student_list = [None] * len(lines)
student_list_dict = [None] * len(lines)
i = 0
for line in lines:
    student_dict = {}
    student_dict[int(line.split()[0])] = line.split()[1]
    student_list_dict[i] = student_dict
    student_list[i] = line.split()
    i = i + 1

print(student_list)
print(student_list_dict)
