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
