'''
Created on 25-Mar-2018

@author: SOURABH GUPTA
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