'''
@author: SOURABH GUPTA
'''
'''
Accept two strings 'string1' and 'string2' as an input from the user. Generate a resultant string,
such that it is a concatenated string of all upper case alphabets from both the strings in the order they appear.
Print the actual and the resultant strings.Note:
Each character should be checked if it is a upper case alphabet and then it should be concatenated to the resultant string.
Sample Input:
string1: I Like C
string2: Mary Likes Python
Output: ILCMLP
'''
str1 = input("Input first string")
str2 = input("Input second string")
str3 = ""
for ch in str1+str2:
    if ch.isupper() == True:
        str3 = str3 + ch
print(str1)
print(str2)
print(str3)
