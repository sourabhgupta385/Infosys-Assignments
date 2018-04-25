'''
@author: SOURABH GUPTA
'''
'''
Given below is a dictionary 'customer_details' representing customer details from a Retail Application.
Customer Id is the key and Customer Name is the value. 
customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
Write Python code to perform the operations mentioned below:
a)Print details of customers.
b)Print number of customers.
c)Print customer names in ascending order.
d)Delete the details of customer with customer id = 1005 and print updated dictionary.
e)Update the name of customer with customer id = 1003 to "Mary" and print updated dictionary.
f)Check whether details of customer with customer id = 1002 exists in the dictionary.
'''
customer_details = { 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
print(customer_details)
print(customer_details.__len__())
print(sorted(customer_details.values()))
customer_details.__delitem__(1005)
print(customer_details)
customer_details.__setitem__(1003, "Marry")
print(customer_details)
print(customer_details.__contains__(1002))
