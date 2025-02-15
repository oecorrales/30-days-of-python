# Equal to
a = 5
b = 5
print(a == b)  # True

# Not equal to
a = 5
b = 3
print(a != b)  # True

# Greater than
a = 7
b = 5
print(a > b)  # True

# Less than
a = 3
b = 5
print(a < b)  # True

# Greater than or equal to
a = 5
b = 5
print(a >= b)  # True

# Less than or equal to
a = 3
b = 5
print(a <= b)  # True

# Chaining comparison operators
a = 5
b = 3
c = 7

# Using all different operators in chaining
print(a > b < c)  # True, because 5 > 3 and 3 < 7
print(a == b < c)  # False, because 5 is not equal to 3
print(a != b >= c)  # False, because 3 is not greater than or equal to 7
print(a <= b < c)  # False, because 5 is not less than or equal to 3
print(a >= b <= c)  # True, because 5 >= 3 and 3 <= 7