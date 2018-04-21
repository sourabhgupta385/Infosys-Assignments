'''
@author: SOURABH GUPTA
'''
'''
Accept a string as an input from the user.
Check if the accepted string is palindrome or not. 
•If the string is palindrome,
  print "String is palindrome", otherwise
  print "String is not palindrome".
•Also print the actual and the reversed strings.
'''
str = input("Input a string")
flag = 0
for i in range(0,len(str)):
    if str[i] != str[-i-1]:
        flag = 1
    else:
        pass
if  flag == 0:
    print("String is palindrome")
else:
    print("String is not palindrome")
