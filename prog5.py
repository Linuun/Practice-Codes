# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if b == 0:
  print("Error: Division by zero is not allowed.")
else:
  quotient = a / b
  print (quotient)
