from functools import wraps
from typing import Callable, Any
from datetime import datetime
from time import sleep
import requests


def decorator(custom_message: str = "ALALALA") -> Callable:
    def show_custom_message_deco(func_to_be_called: Callable) -> Callable:
        @wraps(func_to_be_called)
        def inner_function(*args, **kwargs):
            sleep(.1)
            print(custom_message)
            return func_to_be_called(*args, **kwargs)
        return inner_function
    return show_custom_message_deco


def time_it(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


def counter_deco(func: Callable) -> Callable:
    cnt = 0

    @wraps(func)
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"Функция {func} была запущена {cnt} раз")
        return {"executable_object": func, "result": func(*args, **kwargs), "total_run_cnt": cnt}

    return inner


ADMIN_IDS_LIST = [150117822, 440284906, 164549711, 253163342, 383712412, 362857450]


def notifier(recipients_list: list[int]):
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for admin_chat_id in recipients_list:
                requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                             f"chat_id={admin_chat_id}&text={res}")
            return res
        return inner
    return outer


@counter_deco
@time_it
@decorator(custom_message="test")
@notifier(recipients_list=[150117822, 440284906, 164549711, 362857450])
def func_print_message(msg):
    sleep(.2)
    print("Печатаю сообщение!", msg)
    return msg * 10


@notifier(recipients_list=[164549711, 253163342, 383712412, 362857450])
@counter_deco
def simple_func():
    return 1000


# print(func_print_message)
print(func_print_message("123"))
simple_func()
# func_print_message("123")
# print(simple_func())
# simple_func()
# simple_func()
# simple_func()

# first_num = 1
# second_num = 0
# try:
#     print(first_num / second_num)
# except Exception as err:
#     print(err, type(err))
#     raise




