# Program 1: Print Numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Program 2: Sum of Numbers from 1 to 10
sum_numbers = 0
for i in range(1, 11):
    sum_numbers += i
print("Sum:", sum_numbers)

# Program 3: Print Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Program 4: Print Even Numbers between 1 and 20
for i in range(2, 21, 2):
    print(i)

# Program 5: Factorial of a Number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}")

# Program 6: Check if a Number is Prime
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(num/2) + 1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Program 7: Reverse a Number
num = int(input("Enter a number: "))
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print("Reversed Number:", reversed_num)
