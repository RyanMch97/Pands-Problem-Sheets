import sys

def letterFrequency(fileName, letter):

    file = open(fileName, 'r')
    text = file.read()
    return text.count(letter) #I Didn't Understand working with ARGv[], just read normal file
 
print(letterFrequency('ETextFile.txt', 'e'))

