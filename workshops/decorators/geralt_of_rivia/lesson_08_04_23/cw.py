from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps, WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES, partial, update_wrapper
from typing import Callable, List, Any

from workshops.decorators.commander_shepard.lesson_07_04_23.cw import time_it


def show_message_before_function_deco(msg: str):
    def decorator(some_func: Callable):
        print("Декорируем функцию", some_func)

        @wraps(some_func)
        def inner_func(*args, **kwargs):
            print(msg)
            result = some_func(*args, **kwargs)
            return result
        return inner_func
    return decorator


# @show_message_before_function_deco(msg="test")
# def simple_func(param_1, param_2):
#     print("Вызов simple_func с параметрами:", param_1, param_2)
#     return f"Результат работы simple_func с параметрами: {param_1}, {param_2}"


# @show_message_before_function_deco(msg="test1")
# def simple_func_2(param_1):
#     print("Вызов simple_func_2 с параметрами:", param_1)
#     return f"Результат работы simple_func_2 с параметрами: {param_1}"


# print(simple_func)
# simple_func(1, 2)
# simple_func_2(1)


# new_simple_func = show_message_before_function_deco(simple_func, "custom msg")
# new_simple_func_2 = show_message_before_function_deco(simple_func_2, "custom msg2")
# new_simple_func(1, 2)
# new_simple_func_2(1)

# def outer(a):
#     def inner():
#         def super_inner():
#             nonlocal a
#             a += 1
#             print(a)
#
#         super_inner()
#     inner()
#
#
# outer(1)

def time_it(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


@show_message_before_function_deco(msg="задекорировали класс")
class SimpleClass:
    @time_it
    def __call__(self, *args, **kwargs):
        print("вызываю объект класса")


print(SimpleClass)
my_obj = SimpleClass()
my_obj()

import requests


class Notifier(ABC):
    @abstractmethod
    def __call__(self):
        pass


class TelegramNotifier(Notifier):
    def __call__(self, *args, **kwargs):
        URL = "https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?chat_id=362857450&text=TGtest"
        requests.get(URL)


class SmsNotifier(Notifier):
    def __call__(self, *args, **kwargs):
        URL = "https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?" \
              "chat_id=362857450&text=SMStest"
        requests.get(URL)


class EmailNotifier(Notifier):
    def __call__(self, *args, **kwargs):
        URL = "https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?" \
              "chat_id=362857450&text=Emailtest"
        requests.get(URL)


tg_notifier = TelegramNotifier()
sms_notifier = SmsNotifier()
email_notifier = EmailNotifier()


def notifier_deco(notifiers: List[Notifier]):
    def func_deco(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for notifier in notifiers:
                notifier()
            return res
        return inner
    return func_deco


def check_token(token_list: List[str]) -> Callable:
    def deco(func: Callable) -> Callable:
        def inner(token: str, *args, **kwargs) -> Any:
            if token in token_list:
                return func(token=token, *args, **kwargs)
            raise Exception('Wrong Token')
        return inner
    return deco


ALLOWED_TOKENS = [
    "secret token from service one",
    "secret token from service two"
]

ALLOWED_TOKENS_2 = [
    "secret token from service three",
    "secret token from service four"
]


@notifier_deco(notifiers=[tg_notifier, ])
def my_func():
    print("какая-то логика")


@check_token(ALLOWED_TOKENS_2)
@notifier_deco(notifiers=[tg_notifier, sms_notifier, email_notifier])
def my_func_2():
    print("какая-то логика my_func_2")


@check_token(ALLOWED_TOKENS)
@notifier_deco(notifiers=[sms_notifier, email_notifier])
def my_func_3(token: str):
    print("какая-то логика my_func_3")


# my_func()
# my_func_2()
# my_func_3(token="secret token from service one")
