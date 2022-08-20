# Homework, part 1. Step slicing
user_input = input("Type something: ")

words_list = user_input.split()
print(words_list[2::3])


# Homework, part 2. Lists comprehension
my_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]

out_list = [i if type(i) == float
            else i if (type(i) == int and i % 2 == 0)
            else i ** 2 if (type(i) == int and i % 2 != 0)
            else (str(int(i) * 3)) if (type(i) == str and i.isdigit())
            else -1 for i in my_list]
print(out_list)


# Homework, part 2. Using for loop
outbound_list = []
for item in my_list:
    try:
        if isinstance(item, float):
            outbound_list.append(item)

        elif isinstance(item, int) and item % 2 == 0:
            outbound_list.append(item)

        elif isinstance(item, int) and item % 2 != 0:
            outbound_list.append(item ** 2)

        elif isinstance(item, str) and item.isdigit():
            outbound_list.append(int(item) * 3)

        elif isinstance(item, str):
            outbound_list.append(-1)

    except ValueError as error:
        print(f"Error: {error}.")

print(outbound_list)
