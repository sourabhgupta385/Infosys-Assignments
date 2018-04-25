'''
@author: SOURABH GUPTA
'''
'''
Consider the scenario from "Variety Retail Store" discussed in 'List' section.
The list of furniture available with its respective cost is given below:
A customer can order any furniture in any quantity.
If the required furniture is available in the furniture list(given above) and quantity to be purchased is greater than zero,
 then bill amount should be calculated.
In case of invalid values for furniture required by the customer and quantity to be purchased,
display appropriate error message and consider bill amount to be 0. 
Initialize required furniture and quantity with diﬀerent values and test the results.
Calculate and display the bill amount to be paid by the customer based on the furniture bought and quantity purchased.
Implement the given scenario using:
1)List of tuples
2)Dictionary
'''
furniture = [('sofa',2000),('dining',8500),('tv',4599),('cupboard',13920)]
required_furniture = input("Enter the furniture")
required_quantity = int(input("Enter the quantity"))
bill_amount = 0

for i in range(0,len(furniture)):
    if required_furniture == furniture[i][0]:
        bill_amount = bill_amount + furniture[i][1]*required_quantity
        break
    else:
        bill_amount = 0
if bill_amount == 0:
    print("required furniture is not available in the list")
    print("Amount : ",bill_amount)
else:
    print("Item purchased : ",required_furniture)
    print("Amount : ",bill_amount)
