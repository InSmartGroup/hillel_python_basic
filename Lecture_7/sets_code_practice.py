set_1 = {1, 3, 5, 7, 9}
set_2 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# The .issubset() method checks if the data in a set_1 is being stored in set_2
print(set_1.issubset(set_2))
print(set_2.issubset(set_1))
print()

# The .issuperset() method checks if the data in a set_2 is being stored in set_1
print(set_1.issuperset(set_2))
print(set_2.issuperset(set_1))
print()

# The .union() method checks and combines all the unique elements in two sets
set_union = set_1.union(set_2)
print(set_union)
print()

# The .intersection() method returns all objects that are common for both sets
print(set_1.intersection(set_2))
print(set_2.intersection(set_1))
print()

# The .difference() method returns all objects that are not presented in a specified set
print(set_1.difference(set_2))
print(set_2.difference(set_1))
print()

# The .symmetric_difference() method compares both sets and returns all objects that are not presented in one of those
print(set_1.symmetric_difference(set_2))
print(set_2.symmetric_difference(set_1))
print()

# The .add() method adds an object to a set
set_1.add(0)
print(set_1)
print()

# The .discard() method removes an object from a specified set
set_2.discard(0)
print(set_2)
print()
