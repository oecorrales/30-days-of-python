# and operator
a = True
b = False
print("a and b:", a and b)  # False

a = True
b = True
print("a and b:", a and b)  # True

# or operator
a = True
b = False
print("a or b:", a or b)  # True

a = False
b = False
print("a or b:", a or b)  # False

# not operator
a = True
print("not a:", not a)  # False

a = False
print("not a:", not a)  # True

# Combining logical operators
a = True
b = False
c = True
print("a and b or c:", a and b or c)  # True

a = False
b = True
c = False
print("a or b and c:", a or b and c)  # False