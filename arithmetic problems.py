# Program 1: Addition of Two Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_result = num1 + num2
print(f"Sum: {sum_result}")

# Program 2: Subtraction of Two Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
difference_result = num1 - num2
print(f"Difference: {difference_result}")

# Program 3: Multiplication of Two Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
product_result = num1 * num2
print(f"Product: {product_result}")

# Program 4: Division of Two Numbers
num1 = int(input("Enter the numerator: "))
num2 = int(input("Enter the denominator: "))
if num2 != 0:
    quotient_result = num1 / num2
    print(f"Quotient: {quotient_result}")
else:
    print("Cannot divide by zero.")

# Program 5: Modulo Operation
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 != 0:
    remainder_result = num1 % num2
    print(f"Remainder: {remainder_result}")
else:
    print("Cannot perform modulo with zero.")

# Program 6: Square of a Number
num = int(input("Enter a number: "))
square_result = num ** 2
print(f"Square: {square_result}")

# Program 7: Cube of a Number
num = int(input("Enter a number: "))
cube_result = num ** 3
print(f"Cube: {cube_result}")

# Program 8: Average of Three Numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
average_result = (num1 + num2 + num3) / 3
print(f"Average: {average_result}")

# Program 9: Check if a Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Program 10: Check if a Number is Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")
