# Define two numbers
num1 = 10
num2 = 5

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Print results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Using conditional statements
if addition > 20:
    print("The result of addition is greater than 20.")
elif addition == 20:
    print("The result of addition is exactly 20.")
else:
    print("The result of addition is less than 20.")

if subtraction > 0:
    print("The result of subtraction is positive.")
elif subtraction == 0:
    print("The result of subtraction is zero.")
else:
    print("The result of subtraction is negative.")
    
# Checking if division by zero would occur
if num2 != 0:
    print("Division is defined since num2 is not zero.")
else:
    print("Division by zero is not defined.")
