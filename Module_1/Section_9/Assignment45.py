'''
@author: SOURABH GUPTA
'''
'''
Consider a Python string:cust_details = "Hello John, your customer id is j181"
1)Find, if the name of the customer is preceded by a pattern "Hello " or "hello "
  (Observe a space after the word)? If pattern is found, print the searched result.
2)Find, if the given string ends with a pattern containing only one alphabet followed by three numbers?
  If pattern is found, print the searched result.
3)Replace the word starting with "j" followed by three numbers to only the number(remove the alphabet).
4)Replace the word "id" with "ID".
The output of the above code is "Hello John, your customer ID is 181"
'''
import re
cust_details = "Hello John, your customer id is j181"
matched1 = re.search("^Hello |^hello ",cust_details)
matched2 = re.search(".\d{3}$",cust_details)
replace1 = re.sub("j\d{3}", "181", cust_details)
replace2 = re.sub("id", "ID", cust_details)
print(matched1.group())
print(matched2.group())
print(replace1)
print(replace2)
