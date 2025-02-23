# if statement
x = 10
if x > 5:
    print("x is greater than 5")

# if-else statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# if-elif-else statement
z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")

# Nested if statements
a = 15
if a > 10:
    if a > 20:
        print("a is greater than 20")
    else:
        print("a is greater than 10 but less than or equal to 20")
else:
    print("a is 10 or less")

# Ternary conditional operator
b = 8
result = "b is even" if b % 2 == 0 else "b is odd"
print(result)

# Logical operators
x = 7
y = 12

# Using 'and' operator
if x > 5 and y > 10:
    print("Both x is greater than 5 and y is greater than 10")
else:
    print("Either x is not greater than 5 or y is not greater than 10")

# Using 'or' operator
if x > 10 or y > 10:
    print("Either x is greater than 10 or y is greater than 10")
else:
    print("Neither x is greater than 10 nor y is greater than 10")

# Using 'not' operator
if not x > 10:
    print("x is not greater than 10")
else:
    print("x is greater than 10")

# Using 'elif' with logical operators
if x > 10 and y > 10:
    print("Both x and y are greater than 10")
elif x > 10 and y <= 10:
    print("x is greater than 10 and y is 10 or less")
elif x <= 10 and y > 10:
    print("x is 10 or less and y is greater than 10")
else:
    print("Both x and y are 10 or less")

