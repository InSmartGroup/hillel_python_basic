# some_str = 'hey there'
#
#
# def capital(name: str):
#     return name.capitalize()
#
#
# print(capital(some_str))
# print(capital('hey there'))
########################################################
# word = 'global'
#
#
# def prt_word():
#     word = 'local'
#     return f"{word}"
#
#
# print(prt_word())
# print(word)
########################################################
# name = 'Greg'
#
#
# def greet():
#     global name
#     name = 'Steve'
#     return f"{name}"
#
#
# print(name)
# print(greet())
########################################################
def factorial(num):
    factor = 1
    for i in range(1, num + 1):
        factor = factor * i
    return f"{num} factorial is {factor}"


print(factorial(5))
