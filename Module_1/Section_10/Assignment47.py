'''
@author: SOURABH GUPTA
'''
'''
Consider a string:my_string = “””Strings are amongst the most popular data types in Python.
We can create the strings by enclosing characters in quotes. Python treats single quotes the same as double quotes.”””
1) Write a Python program to count the number of occurrences of word "String" in the given string ignoring the case.
2) Write a function "count_words" to print the count of occurrences of a word:
    a) which end with "on". (e.g. Python)
    b) which have "on" in between the ﬁrst and last characters (e.g. amongst)
'''
import random
my_string = '''Strings are amongst the most popular data types in Python.
               We can create the strings by enclosing characters in quotes.
               Python treats single quotes the same as double quotes.'''

my_string = my_string.lower()
count_string = my_string.count("string")
print("Count of word 'string'",count_string)

def count_words(my_string):
    count_end_with_on = 0
    count_contain_on = 0
    words = my_string.split()
    for word in words:
        if word.endswith("on") | word.endswith("on."):
            count_end_with_on = count_end_with_on + 1
        if word.find("on") > 0 and word.endswith("on") == False and word.endswith("on.") == False:
            count_contain_on = count_contain_on + 1
    print("Words that ends with 'on' : ",count_end_with_on)
    print("Words that contain 'on' : ",count_contain_on)

count_words(my_string)
