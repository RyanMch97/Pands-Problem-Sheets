import math
  
#Defintion for program
def newton(Number, NumbersList = 10000025):

    Number = float(Number) 

    for i in range(NumbersList): 

        Number = 0.5 * (Number + InputNumber / Number) 

    return Number

InputNumber=int(input("Enter first number:"))
print("Square root of fmy number:",newton(InputNumber))