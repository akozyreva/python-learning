def new_decorator(original_func):
    def wrap_func():
        print("Some extra coe, before the original func")
        original_func()
        print("Some extra code, after the original func")

    return wrap_func


@new_decorator
def func_needs_decorator():
    print("I want to be decorated")


func_needs_decorator()
