# pass imitates a block of code
if 3 != 3:
    print('Oh no!')
else:
    pass


result = int(15 / 2)
if result == 7:
    print('okay')

if result := int(15 / 2) == 7:
    print('okay')


# One liners
operand = 3
result = operand ** 0.5 if operand >= 3 else operand ** 2
print(f"{result=}")


# Using match-case
response_code = 200
match response_code:
    case 200:
        print('okay')
    case 500:
        print('Internal Server Error')
    case _:  # default case is recommended
        print('Default case for all other results')


# Using match-case with additional requirements
response_code = 300
etalon_code = 201
match response_code:
    case 200 if response_code == etalon_code:
        print('okay')
    case 500:
        print('Internal Server Error')
    case 300 | 301 | 302 | 303:
        print('Some 300th codes.')
    case _:  # default case is recommended
        print('Default case for all other results')


# Try - except
if 3 != 2:
    try:
        print('Yup')
    except:
        print('Nope')

try:
    i = 3 / 0
    print(i)
except ZeroDivisionError:
    print('Nope')


# Try - except - else
try:
    i = 3 / 1
    print(i)
except ZeroDivisionError:
    print('Nope')
else:  # the else statement will always be executed if the try statement was True
    print('Absolutely')


# Create the script to work with errors
try:
    num = 3
    divider = 0
    print(num / divider)
# except ZeroDivisionError:
#     print('You can\'t divide by zero')
except Exception as error:
    print(f"Unknown error: {error}.")
except NameError as nameerror:
    print(f"Unexpected error: {nameerror}.")


# Try - except - finally
try:
    num = 3 / 0
    print(num)
except ZeroDivisionError as error:
    print(f"Error: {error}.")
finally:  # finally will always be executed
    print("You're cool, bro!")
