from expressionlogic import *

operation = input('''
            Please type in the operation you would like to complete.
            + for addition
            - for subtraction
            * for multiplication
            / for division
            ''')

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

if operation == '+':
  solution = add(num1, num2)
  print("the solution to " + str(num1) + operation + str(num2) + " is " + str(solution))

elif operation == '-':
  solution = subtract(num1,num2)
  print("the solution to " + str(num1) + operation + str(num2) + " is " + str(solution))


elif operation == '*':
  solution = multiply(num1,num2)
  print("the solution to " + str(num1) + operation + str(num2) + " is " + str(solution))


elif operation == '/':
  solution = division(num1,num2)
  print("the solution to " + str(num1) + operation + str(num2) + " is " + str(solution))

  
else: 
  print('You have not typed a valid operator, please try again')