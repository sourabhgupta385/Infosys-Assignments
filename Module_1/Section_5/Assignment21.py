'''
@author: SOURABH GUPTA
'''
'''
The "Variety Retail Store" sells diﬀerent varieties of Furniture to the customers.
The list of furniture available with its respective cost is given below:
The furniture and its corresponding cost should be stored as a list.
A customer can order any furniture in any quantity (the name and quantity of the furniture will be provided).
If the required furniture is available in the furniture list(given above) and quantity to be purchased is greater than zero,
then bill amount should be calculated.
In case of invalid values for furniture required by the customer and quantity to be purchased,
display appropriate error message and consider bill amount to be 0.
Initialize required furniture and quantity with diﬀerent values and test the results.
Write a Python program to calculate and
display the bill amount to be paid by the customer based on the furniture bought and quantity purchased.

'''
furniture = ['sofa','dining','tv','cupboard']
cost = [2000,8500,4599,13920]

required_furniture = input("Enter the furniture")
required_quantity = int(input("Enter the quantity"))
bill_amount = 0
for i in range(0,len(furniture)):
    if required_furniture == furniture[i]:
        bill_amount = bill_amount + cost[i]*required_quantity
        break
    else:
        bill_amount = 0
if bill_amount == 0:
    print("required furniture is not available in the list")
    print("Amount : ",bill_amount)
else:
    print("Item purchased : ",required_furniture)
    print("Amount : ",bill_amount)
