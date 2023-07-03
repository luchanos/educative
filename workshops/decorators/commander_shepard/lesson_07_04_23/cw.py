from typing import Callable, Any
from datetime import datetime
from time import sleep


def decorator(custom_message: str = "ALALALA") -> Callable:
    def show_custom_message_deco(func_to_be_called: Callable) -> Callable:
        def inner_function(*args, **kwargs):
            sleep(1)
            print(custom_message)
            return func_to_be_called(*args, **kwargs)
        return inner_function
    return show_custom_message_deco


def time_it(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


@time_it
@decorator(custom_message="test")
def func_print_message(msg):
    sleep(.2)
    print("Печатаю сообщение!", msg)
    return msg * 10


func_print_message("fffff")
# func_print_message
# time_it(decorator("test")(func_print_message))("msg")


@decorator(custom_message="test2")
def print_advertisement():
    print("Покупайте наших котиков!")
    return 1


# print_advertisement()




# func_print_message_new = show_custom_message_deco(func_to_be_called=func_print_message, custom_message="TEST1")
# print_advertisement_new = show_custom_message_deco(func_to_be_called=print_advertisement, custom_message="TEST2")
# print(func_print_message_new(123))
# print(print_advertisement_new())

b = []
c = 123


def outer2(a=1):

    def outer():
        def inner():
            print(a)

        inner()
    outer()


# outer2()
