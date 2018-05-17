'''
@author: SOURABH GUPTA
'''
from random import shuffle
from string import punctuation
def open_file(file_name):
    try:
        my_file = open(file_name + '.txt', "r")
        sentence = my_file.read()
        return sentence
    except IOError:
        print("File Not Found. Enter the correct name")

def shuffle_word(word):
    first = word[0]
    if word[-1] in punctuation:
        last = word[-2] + word[-1]
        word = list(word[1:word.__len__()-2])
    else:
        last = word[-1]
        word = list(word[1:word.__len__()-1])
    shuffle(word)
    result = first + ''.join(word) + last
    return result

def final_sentence(sentence):
    words = sentence.split()
    scrambled_sentence = ""
    for word in words:
        if word.__len__() <=3 :
            scrambled_sentence = scrambled_sentence + " " + word
        else:
            scrambled_sentence = scrambled_sentence + " " + shuffle_word(word)
    return scrambled_sentence.lstrip()

def output_file(file_name,scrambled_sentence):
    try:
        result = open(file_name + 'Scrambled.txt',"w")
        result.write(scrambled_sentence)
        print("Scrambled sentence written successfully!")
    except IOError:
        print("Error in writing in file")

file_name = input("Enter the file name(do not enter the extension) : ")
sentence = open_file(file_name)
scrambled_sentence = final_sentence(sentence)
output_file(file_name, scrambled_sentence)
