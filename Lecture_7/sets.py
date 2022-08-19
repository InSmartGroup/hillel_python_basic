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
