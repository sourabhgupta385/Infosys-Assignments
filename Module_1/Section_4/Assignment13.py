'''
@author: SOURABH GUPTA
'''
'''
Consider the scenario of retail store management again.
The store provides discount for all bill amounts based on the criteria below:
    Bill Amount         Discount %
    >=1000                  5
    >=500 & <1000           2
    >0 & <500               1
Write a Python program to ﬁnd the net bill amount after discount.
Assume that bill amount will be always greater than zero.
Extend the above program to validate the customer id.
Customer ids in the range of 101 and 1000 (bothinclusive) should only be considered valid.
'''
customer_id = 950
customer_name = "Rahul"
bill_amount = 2000

if customer_id >= 101 and customer_id <= 1000:
    if bill_amount >= 1000:
        bill_amount = bill_amount - bill_amount * 5/100
    elif bill_amount >= 500 and bill_amount < 1000:
        bill_amount = bill_amount - bill_amount * 2/100
    else:
        bill_amount = bill_amount - bill_amount * 5/100
print("customer_id : ",customer_id)
print("customer_name : ",customer_name)
print("bill_amount : ",bill_amount)
