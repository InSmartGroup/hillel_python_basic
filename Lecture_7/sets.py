import itertools

input_1 = set(input("Type anything: "))
input_2 = set("Type anything again: ")

letters = set()
digits_input_1 = set()
digits_input_2 = set()

for char in itertools.chain(input_1, input_2):
    if char.isalpha():
        letters.add(char)
    elif char.isdigit():
        if char in input_1:
            digits_input_1.add(char)
        elif char in input_2:
            digits_input_2.add(char)

print(letters)
print(digits_input_1.symmetric_difference(digits_input_2))

# Set 'update' method
set_1 = {1, 3, 5, 7}
set_2 = {2, 4, 6, 10}

set_1.update(set_2)
print(set_1)

# Useful set operators
set_3 = {'hi', 0, 1, 2, 3, 5, 6, 7, 9}
set_4 = {2, 4, 6, 'sym', 7, 8, 9, 10, 'num'}
set_5 = {0, 1, 2, 3, 'sym', 5, 8, 11}

# Union
print(set_3 | set_4 | set_5)

# Intersection
print(set_3 & set_4 & set_5)

# Difference
print(set_3 - set_4 - set_5)

# Symmetric difference
print(set_3 ^ set_4 ^ set_5)
