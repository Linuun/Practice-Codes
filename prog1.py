# Create a program that ask user to input 2 numbers. Print the bigger number.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print (f"The bigger number is {a}")
elif a == b:
    print ("The numbers are equal")
else:
    print  (f"The bigger number is {b}")