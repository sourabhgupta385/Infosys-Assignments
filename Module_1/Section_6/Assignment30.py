'''
@author: SOURABH GUPTA
'''
'''
Write a Python program to implement the following (Use Recursion):
1.Print ﬁrst 'n' multiples of 3, where 'n' is taken as an input from the user. The multiples should be printed from ﬁrst to last.
2.Reverse a string. Print the original and reversed string.
3.Check if the given string is palindrome.
If yes,
print "String is palindrome"
otherwise
print "String is not palindrome".
'''
#first n multiples of 3
def multiple(number):
    if number == 1:
        result.append(3)
        return 0
    else:
        result.append(number*3)
        return multiple((number - 1))

number = int(input("Enter a number"))
result = []
if number > 0:
    multiple(number)
    for i in range(1,result.__len__() + 1):
        print(result[-i], end=" ")
else:
    print("Invalid input...Enter a positive number")

#reversal of string
def reverse(str1):
    if str1 == '':
        return str1
    else:
        return reverse(str1[1:]) + str1[0]

print(reverse(input("Enter a string")))


#Palindrome

def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=input("Enter string:")
if(is_palindrome(a) == True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
