user_input = input("Type your text here: ")

spaces = []
vowels = []
digits = []

for index, letter in enumerate(user_input):

    if letter == " ":
        spaces.append(index)

    if letter in "aouei":
        vowels.append(letter)

    try:
        if letter.isdigit():
            if user_input[index + 1].isdigit() and user_input[index + 2].isdigit():
                digits.append(user_input[index])
                digits.append(user_input[index + 1])
                digits.append(user_input[index + 2])
                print("The loop has been terminated: 3 digits in a row.")
                break
            else:
                print("The loop has been processed.")
    except IndexError as error:
        print(f"The loop has been terminated: {error}.")

print()
print(f"Uppercase input: {user_input.upper()}")
print(f"Indexes of spaces: {', '.join(str(i) for i in spaces)}")
print(f"3-in-a-row digits: {', '.join(str(i) for i in digits)}")


