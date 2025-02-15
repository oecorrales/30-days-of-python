# Step 1: Obtain two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Select the operation
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

# Step 3: Execute the operation
if operation == '1':
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation == '2':
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation == '3':
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")