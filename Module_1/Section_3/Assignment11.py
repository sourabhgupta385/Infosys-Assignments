'''
Created on 24-Mar-2018

@author: SOURABH GUPTA
'''
'''
Consider two variables 'a' and 'b' in Python such that a = 4 and b = 5.
Swap the values of 'a' and 'b' without using a temporary variable.
Print the values of 'a' and 'b' before and after swapping.
'''
a = 4
b = 5
print ("a = ",a,"b = ",b)
a = a + b
b = a - b
a = a - b
print ("a = ",a,"b = ",b)

'''
Consider the scenario of processing marks of a student in ABC Training Institute.
John, the student of ﬁfth grade takes exams in three diﬀerent subjects.
Create three variables to store the marks obtained by John in three subjects.
Find and display the average marks scored by John.
'''
sub1 = 98
sub2 = 87
sub3 = 76
avg_marks = (sub1+sub2+sub3)/3
print("Average Marks : ",avg_marks)
sub2 = 75
print("Average Marks : ",avg_marks)

'''
Given the value of radius of a circle.
Write a Python program to calculate the area and perimeter of the circle.Display both the values.
'''
radius = 10
area = 3.14 * radius * radius
perimeter = 2 * 3.14 * radius
print("Area : ",area,"Perimeter : ",perimeter)

'''
The ﬁnance department of a company wants to compute the monthly pay of its employees.
Monthly pay shouldbe calculated as mentioned in the formula below.
Display all the employee details.
Monthly Pay = Number of hours worked in a week * Pay rate per hour * No. of weeks in a month
•The number of hours worked by the employee in a week should be considered as 40
•Pay rate per hour should be considered as Rs.400
•Number of weeks in a month should be considered as 4
'''
Number_of_hours_worked_in_a_week = 40
Pay_rate_per_hour = 400
No_of_weeks_in_a_month = 4

monthly_pay = Number_of_hours_worked_in_a_week * Pay_rate_per_hour * No_of_weeks_in_a_month
print("Monthly Pay : ", monthly_pay)
