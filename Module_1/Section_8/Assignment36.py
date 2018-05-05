'''
@author: SOURABH GUPTA
'''
'''
You have already created a Python program to implement the following in ﬁle handling section:
1.read a ﬁle.
2.add backslash (\) before every double quote in the ﬁle contents.
3.write it to another ﬁle in the same folder.
4.print the contents of both the ﬁles.
Modify your code to implement Exception handling.
Print appropriate error messages wherever applicable.
'''
try:
    f = open("TestFile1.txt","r")
    sentence = f.read()
    result = open("TestFile2.txt","w")
    for i in range(0,sentence.__len__()):
        if sentence[i] == '"':
            result.write('\\"')
        else:
            result.write(sentence[i])
except IOError:
    print("File Not Found")
else:
    print("Code executed successfully")
