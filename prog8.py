# Create a program that ask user to input 10 numbers. Print how many are odd numbers.
numbers = []

odd = 0
print("Enter 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
    if num % 2 == 1:
        odd += 1

print (f"The odd number/s is/are {odd}")

