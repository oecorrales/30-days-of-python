# Using 'is' operator
a = 10
b = 10
print(a is b)  # True, because both a and b point to the same memory location

# Using 'is not' operator
c = [1, 2, 3]
d = [1, 2, 3]
print(c is not d)  # True, because c and d are different objects in memory

# Using 'is' with None
e = None
print(e is None)  # True, because e is None

# 'is not' with None
f = 5
print(f is not None)  # True, because f is not None

# Using 'is' with strings
g = "hello"
h = "hello"
print(g is h)  # True, because Python optimizes memory usage for small strings

# Using 'is not' with strings
i = "hello"
j = "world"
print(i is not j)  # True, because i and j are different strings