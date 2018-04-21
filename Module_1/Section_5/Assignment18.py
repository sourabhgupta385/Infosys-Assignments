'''
@author: SOURABH GUPTA
'''
'''
Given a string containing both upper and lower case alphabets.
Write a Python program to count the number of occurrences of each alphabet(case insensitive)
and display the same.
Sample Input: ABaBCbGc
Sample Output:
2A
3B
2C
1G
'''
str1 = "ABaBCbGc"
str1 = str1.upper()
d = {}
# count occurances of character
for w in str1:
    d[w] = str1.count(w)
# print the result
for k in sorted(d):
    print (k + ':' + str(d[k]))
