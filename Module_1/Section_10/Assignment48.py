'''
@author: SOURABH GUPTA
'''
'''
Consider the price list of various items in the Retail Store:
item_price = [1050, 2200, 8575, 485, 234, 150, 399]
Customer John wants to know the:
1.Price of costliest item sold in retail store
2.Number of items in the Retail store
3.Prices of items in increasing order
4.Prices of items in descending order
Implement the above mentioned business requirements using built-in List functions.
'''
import math
item_price = [1050, 2200, 8575, 485, 234, 150, 399]
print("max price : ",max(item_price))
print("no of items : ", len(item_price))
print("price in increasing order : ",sorted(item_price))
print("price in decreasing order : ", sorted(item_price, reverse = True))
