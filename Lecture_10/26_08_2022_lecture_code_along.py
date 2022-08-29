def main_decor(func_to_decor):
    print("Inside start main_decor")

    def warapper():
        print("Inside start wrapper")
        func_to_decor()
        print("Inside end wrapper")

    print("Inside finish main_decor")

    return warapper


def main_func():
    print("Inside main function")


# main_func()  # usual call
decorated_main_func = main_decor(main_func)
decorated_main_func()  # decorated call