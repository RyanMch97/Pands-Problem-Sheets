inputString = input('enter a string:')
lenghtOfString = len(inputString)
print('The lenght of {} is {}'.format(inputString, lenghtOfString))

SecondLetter = inputString[::2]
print('The reverse of {} is {}'.format(inputString, SecondLetter))

ReverseSecondLetter = SecondLetter[::-1]
print(ReverseSecondLetter)