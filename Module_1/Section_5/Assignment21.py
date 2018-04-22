'''
Created on 25-Mar-2018

@author: SOURABH GUPTA
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