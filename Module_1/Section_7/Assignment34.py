'''
@author: SOURABH GUPTA
'''
'''
Consider a ﬁle 'rhyme.txt' with following text:

Jingle bells jingle bells
Jingle all the way
Oh what fun it is to ride
In a one horse open sleigh
Jingle bells jingle bells
Jingle all the way

Write a Python program to count the words in the ﬁle using a dictionary (use space as a delimiter).
Find unique words and the count of their occurrences(ignoring case).
Write the output in another ﬁle "words.txt" at the same location.

'''
result = open("rhyme.txt","r")
lines = result.read()
lines = lines.lower()
tokens = []
d = {}
for token in lines.split():
    tokens.append(token)
    if token in d:
        d[token] +=1
    else:
        d[token] = 1
print(len(tokens))

f = open("words.txt","w")
for k in d:
    f.write(str(k)+ " : " +str(d[k]) + "\n")
