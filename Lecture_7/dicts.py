# Part 1. ASCII table
ascii_dict = {i: chr(i) for i in range(0, 128)}

print(ascii_dict)


# Part 2. User input
user_input = input("Type something: ")
user_password = int(input("Type 1-digit number: "))

encoded_input = []

letters = {letter: index + 1 for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}

for letter in user_input:
    if letter in letters:
        new_index = letters[letter] + user_password
        encoded_input.append(list(letters.keys())[list(letters.values()).index(new_index)])

print(f"Your encoded input is: {''.join(encoded_input)}")
