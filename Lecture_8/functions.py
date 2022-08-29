# Exercise 1. Adding numbers in a specified range
def sum_in_range(start, end):
    if start > end:
        new_start = end
        end = start
        values = sum(range(new_start, end + 1))
    else:
        values = sum(range(start, end + 1))
    return values


print(sum_in_range(10, 5))
print(sum_in_range(71, 13))
print(sum_in_range(0, 21))
print(sum_in_range(7, 58))


# Exercise 2. Seconds to 'dd:hh:mm:ss' format
def seconds_to_days(seconds):
    result = []
    time_intervals = [
        ["Years", 60 * 60 * 24 * 7 * 4 * 12],
        ['Months', 60 * 60 * 24 * 7 * 4],
        ['Weeks', 60 * 60 * 24 * 7],
        ['Days', 60 * 60 * 24],
        ['Hours', 60 * 60],
        ['Minutes', 60],
        ['Seconds', 1],
    ]
    for name, count in time_intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append(f"{value} {name}")
    return ", ".join(result).capitalize()


print(seconds_to_days(113725))
print(seconds_to_days(189297784))
print(seconds_to_days(27843))


# Exercise 3.1. A sum function using the 'for' loop
def for_loop_sum(numbers):
    counter = 0
    for num in numbers:
        if isinstance(num, int):
            counter += num
        elif isinstance(num, str):
            num = int(num)
            counter += num
    return counter


print(for_loop_sum([1, 2, 3, 4, '5']))
print(for_loop_sum([13, 9, 4, '19', 7, '11']))
print(for_loop_sum([72, 1, '21', 3, 8]))


# Exercise 3.2. A sum function using the 'while' loop
def while_loop_sum(numbers):
    result = 0
    while numbers:
        result = sum(numbers)
        break
    return result


print(while_loop_sum([72, 1, 21, 3, 8]))
print(while_loop_sum(list(range(1, 21))))
print(while_loop_sum(list(range(1, 101, 3))))

# Exercise 3.3. A recursive function
def recursive_sum(values: list):
    if len(values) == 0:
        return 0
    else:
        return values[0] + recursive_sum(values[1:])


print(recursive_sum([1, 2, 3, 4, 5]))
print(recursive_sum([1, 3, 5, 7, 9, 11]))

# Exercise 4. The Fibonacci function
def fibonacci(value):
   sequence = []
   num1, num2 = 0, 1
   for i in range(1, value + 1):
      sequence.append(i)
      num1, num2 = num2, num1 + num2
   return f"Sum: {num2}, sequence: {sequence}"


print(fibonacci(14))
print(fibonacci(17))

# Exercise 5. Decorators
def main_decorator(func_to_decor):
    def tomato():
        print('tomato')

    def meat():
        print('meat')

    def cheese():
        print('cheese')

    def bread():
        print('bread')

    return tomato(), meat(), cheese(), bread()


def main_func():
    return None


main_decorator(main_func())
