# none_obj = None
# print(none_obj, type(none_obj))

# # Strings are immutable
# str_1 = 'this is a qwerty string' + ', ' + 'DIV'
# print(str_1)

# print(str_1[0])
# print(str_1[-1])
# print(str_1[3])
# print(str_1[0:7])  # the last symbol in a slice isn't included
# print(str_1[:9])
# print(str_1[:])
# print(str_1[10:100])
# print(str_1[500:1000])
# print(str_1[::2])
# print(str_1[::5])
# print(str_1[::-1])  # returns a reversed string

# String methods
my_str = 'Hey guys, this is a string'
print(len(my_str))  # returns the number of characters in a string
print(bool(len("")))  # Zero in Boolean logic always returns False
print(my_str.replace('this', '!!!THAT!!!'))
print(my_str.isdigit())  # Returns True only is a string consists of numeric values
print(my_str.isalpha())  # Returns True only is a string consists of alphabetic values
print(my_str.isalnum())  # Returns True only is a string consists of numeric or alphabetic values
print(my_str.capitalize())  # Formats the string and makes it good to read
print(my_str.upper())  # Makes a string all-uppercase
print(my_str.lower())  # Makes a string all-lowercase
print(my_str.swapcase())  # Swaps font case in a string
print(my_str.title())  # Makes every word in a string uppercase
print(my_str.startswith('h'))  # Returns True or False if the string starts with a specified letter
print(my_str.endswith('g'))  # Returns True or False if the string ends with a specified letter
