'''
@author: SOURABH GUPTA
'''
'''
Consider a scenario of managing student details in ABC Training Institute.
Write a Python program to implement the business requirements mentioned below:
a)Accept student_id and validate whether it contains only digits.
b)If student _id is valid, accept student_name from the user and validate whether it contains only alphabets.
c)If student_name is valid, accept fees_amount paid by the student:
    1.Decimal point is optional in fees_amount(can have maximum one decimal point)
    2.Only two digits are allowed after decimal point
d)If invalid data is entered in any of the above steps, display appropriate error messages.
  Else, create an email_id for student as student_name@ABC.com. Assume there are no duplicate names.
e)Perform above validations using Regular Expressions and print details of the student:
  student_id, student_name, fees_amount, email_id
'''
import re
student_id = input("Enter student id")
matched_student_id = re.match('[0-9]+$',student_id)
if matched_student_id:
    student_id = int(student_id)
    student_name = input("Enter student name")
    matched_student_name = re.match('^[A-Za-z]*$',student_name)
    if matched_student_name:
        fees_amount = input("Enter the fees amount")
        matched_fees_amount = re.match('^[0-9]*(\.\d{2})?$',fees_amount)
        if matched_fees_amount:
            student_email_id = student_name + '@ABC.com'
            print("student_id : ",student_id)
            print("student_name : ",student_name)
            print("fees_amount : ",fees_amount)
            print("student_email_id : ",student_email_id)
        else:
            print("Enter the fees amount in proper format")
    else:
        print("Invalid format for name")
else:
    print("Student id must contain digits only")
