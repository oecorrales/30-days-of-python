
# Conditional Statements
x = 1
y = 2

if x < y:
    print("x is less than y")
else:
    print("x is not less than y")
# Output: x is less than y

# Logical Operations
a = True
b = False
print(a and b)  # False, because both need to be True for 'and'
print(a or b)   # True, because at least one is True for 'or'
print(not a)    # False, inverts the value of a

# Conversion from other types
print(bool(1))         # True, since non-zero numbers are True
print(bool(0))         # False, zero is considered False
print(bool("Hello"))   # True, non-empty strings are True
print(bool(""))        # False, empty strings are False
print(bool([1,2,3]))   # True, non-empty lists are True
print(bool([]))        # False, empty lists are False

# Ternary Expression
result = "Even" if x == 2 else "Odd"
print(result)  # "Even"