operation = input('''
            Please type in the operation you would like to complete.
            + for addition
            - for subtraction
            * for multiplication
            / for division
            ''')

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the first number: '))

if operation == '+':
  def add (num1, num2):
    return num1 + num2

elif operation == '-':
  def subtract(num1, num2):
    return num1 - num2

elif operation == '*':
  def multiply(num1, num2):
    return num1 * num2

elif operation == '/':
  def division(num1, num2):
    return num1/num2
  
else: 
  print('You have not typed a valid operator, please try again')