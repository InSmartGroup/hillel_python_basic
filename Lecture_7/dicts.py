# Part 1. ASCII table
ascii_dict = {i: chr(i) for i in range(0, 128)}

print(ascii_dict)


# Part 2. User input. Version 1
user_input = input("Type something: ")
user_password = int(input("Type 1-digit number: "))

encoded_input = []

letters = {letter: index + 1 for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}

for letter in user_input:
    if letter in letters:
        new_index = letters[letter] + user_password
        encoded_input.append(list(letters.keys())[list(letters.values()).index(new_index)])

print(f"Encoded word: {''.join(encoded_input)}")


# Part 2. User input. Version 2
user_input = input("Type something: ")
user_password = int(input("Enter the shift code: "))

letters = {letter: index + 1 for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}

keys = list(letters.keys())

values = list(letters.values())

new_word = []

for letter in user_input:
    if letter in keys:
        new_position = keys.index(letter) + user_password
        new_letter = keys[new_position]
        new_word.append(new_letter)

print(f"Encoded word: {''.join(new_word)}")
