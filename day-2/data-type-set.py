x = {"lorem", "ipsum", "dolor"} # set

y = frozenset({"lorem", "ipsum", "dolor"}) # frozenset

print(x) # Output: {'dolor', 'lorem', 'ipsum'}

print(y) # Output: frozenset({'dolor', 'lorem', 'ipsum'})

x.add("sit")

print(x) # Output: {'sit', 'ipsum', 'dolor', 'lorem'}

y.add("sit") # AttributeError: 'frozenset' object has no attribute 'add'