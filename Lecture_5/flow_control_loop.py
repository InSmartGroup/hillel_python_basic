list_of_actions = ['+', '-', '/', '*', '**', '//', '%']

comparison = ''

while True:
    operand_1 = input("Enter operand 1: ")
    if operand_1 == 'exit':
        print("Terminating the program.")
        break

    operand_2 = input("Enter operand 2: ")
    if operand_2 == 'exit':
        print("Terminating the program.")
        break

    action = input("Type +, -, /, or * to perform operation: ")
    if action == 'exit':
        print("Terminating the program.")
        break

    try:
        operand_1 = int(operand_1) if operand_1.isdigit() else float(operand_1)
        operand_2 = int(operand_2) if operand_2.isdigit() else float(operand_2)

    except Exception as error:
        print()
        print(f"Error: {error}.")
        print("Please use integers or floating point numbers.")

    if action not in list_of_actions:
        print()
        print("Action is not defined.\nPlease use:\n\t+ to add\n\t- to subtract\n\t/ to divide\n\t* to multiply \
              \n\t** to power\n\t// to use floor division\n\t% to use modulus division")

    elif action == '+':
        print()
        result = operand_1 + operand_2
        print(f"Addition result is {result}")

    elif action == '-':
        print()
        result = operand_1 - operand_2
        print(f"Subtraction result is {result}")

    elif action == '/':
        try:
            print()
            result = operand_1 / operand_2
            print(f"Division result is {result}")
        except ZeroDivisionError:
            print("You can't divide by zero.")

    elif action == '*':
        print()
        result = operand_1 * operand_2
        print(f"Multiplication result is {result}")

    elif action == '**':
        print()
        result = operand_1 ** operand_2
        print(f"Power result is {result}")

    elif action == '//':
        print()
        result = operand_1 // operand_2
        print(f"Floor division result is {result}")

    elif action == '%':
        print()
        result = operand_1 % operand_2
        print(f"Modulus division result is {result}")

    if action not in list_of_actions:
        comparison = 'Unable to compare operands.'
    else:
        comparison = f"{operand_1} {action} {operand_2}"

    print()
