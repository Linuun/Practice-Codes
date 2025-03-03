# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
numbers = []

sum = 0
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    sum += num

print (f"The sum of all the numbers is {sum}")