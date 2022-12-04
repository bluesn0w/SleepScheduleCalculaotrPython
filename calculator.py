from cgitb import reset
import string

#Calculator made by bluesn0w in python while learning programming


#Definning information for rules for input
not_allowed = list(string.ascii_letters)
calculation_methods = ["+","-","*","/"]
allowed = False


while allowed == False:
    first_number = input("Enter your first number: ")
    for n in first_number:
        if n in not_allowed:
            print("not a number!")
            first_number == 0
        else:
            allowed = True

first_number = int(first_number)

allowed = False

while allowed == False:
    calculation = input("+ = add\n- = substract\n* = multiply\n/ = divide\nHow do you want to calculate: ")
    for n in calculation:
        if n in calculation_methods:
            allowed = True
        else:
            print("invalid input")
            break

allowed = False

while allowed == False:
    second_number = input("Enter your second number: ")
    for n in second_number:
        if n in not_allowed:
            print("not a number!")
            second_number == 0
        else:
            allowed = True

second_number = int(second_number)

#Calculation of the input and printing results

if calculation == "+":
    result = (first_number + second_number)
    print(result)

if calculation == "-":
    result = (first_number - second_number)
    print(result)

if calculation == "*":
    result = (first_number * second_number)
    print(result)

if calculation == "/":
    result = (first_number / second_number)
    print(result)



