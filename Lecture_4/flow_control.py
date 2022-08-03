operand_1 = input("Enter operand 1: ")
operand_2 = input("Enter operand 2: ")
action = input("Type +, -, /, or * to perform operation: ")

list_of_actions = ['+', '-', '/', '*', '**', '//', '%']

comparison_1 = ''
comparison_2 = ''


try:
    operand_1 = int(operand_1) if operand_1.isdigit() else float(operand_1)

except Exception as error:
    print()
    print(f"Error: {error}.")
    print("Please use integers or floating point numbers.")


try:
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
    comparison_1 = 'Unable to compare operands.'
elif operand_1 > operand_2:
    comparison_1 = f'It\'s greater than operand 2 by {operand_1 - operand_2}'
elif operand_1 < operand_2:
    comparison_1 = f'It\'s less than operand 2 by {operand_2 - operand_1}'
elif operand_1 == operand_2:
    comparison_1 = "Operand 1 is equal to operand 2"

if action not in list_of_actions:
    comparison_2 = 'Unable to compare operands.'
elif operand_2 > operand_1:
    comparison_2 = f'It\'s greater than operand 1 by {operand_2 - operand_1}'
elif operand_2 < operand_1:
    comparison_2 = f'It\'s less than operand 1 by {operand_1 - operand_2}'
elif operand_2 == operand_1:
    comparison_2 = "Operand 2 is equal to operand 1"


print()
print("Report:")
print(f"\tOperand 1:\n\tType: {type(operand_1)}\n\tComparison: {comparison_1}")
print()
print(f"\tOperand 2:\n\tType: {type(operand_2)}\n\tComparison: {comparison_2}")
