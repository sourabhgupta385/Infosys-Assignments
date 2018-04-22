'''
@author: SOURABH GUPTA
'''
'''
Write a Python program to accept a string 'accepted_string'. Generate a resultant string 'resultant_string' such that
'resultant_string' should contain all characters at the even position of 'accepted_string'(ignoring blank spaces). 
Display 'resultant_string' in reverse order.
accepted_string: An apple a day keeps the doctor away
resultant_string: Aapedyepteotrwy
expected_output: ywrtoetpeydepaA
'''
accepted_string = "An apple a day keeps the doctor away"
expected_string = ""
j = 0
for i in range(0,len(accepted_string)):
    if accepted_string[i] == ' ':
        j = j + 1
        pass
    else:
        if (i+j) % 2 == 0:
            expected_string = expected_string + accepted_string[i]

print(expected_string)
for i in range(1,len(expected_string)+1):
    print(expected_string[-i],end="")
