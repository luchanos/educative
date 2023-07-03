from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps
from time import sleep
from typing import Callable, Any


def calculate_deco(custom_msg: str):
    def metric_deco(func: Callable) -> Callable:
        @wraps(func)
        def func_executor(*args, **kwargs):
            sleep(1)
            print("Сообщение параметризованного декоратора", custom_msg)
            return func(*args, **kwargs)
        return func_executor
    return metric_deco


def time_it(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


# @time_it
# @calculate_deco("test")
@time_it
def func_print_message_second(msg):
    print("Печатаю сообщение!", msg)
    return msg * 10


@time_it
@calculate_deco(custom_msg="test 2")
@time_it
def print_advertisement_second():
    sleep(.5)
    print("Покупайте наших котиков!")


# print(print_advertisement_second)
# func_print_message_second(123)
# print_advertisement_second()


import requests


class Notifier(ABC):
    @abstractmethod
    def __call__(self):
        pass


class TelegramNotifier(Notifier):
    def __call__(self, *args, **kwargs):
        URL = "https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?" \
              "chat_id=362857450&text=TGtest"
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


def notifier_deco(notifiers: list[Notifier]):
    def func_deco(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for notifier in notifiers:
                notifier()
            return res
        return inner
    return func_deco


def check_token(token_list: list[str]) -> Callable:
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








def notifier(notifiers: list[Notifier]):
    def func_deco(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for notifier in notifiers:
                notifier()
            return res
        return inner
    return func_deco


def deco_token(token_list: list[str]) -> Callable:
    def deco(func: Callable) -> Callable:
        def inner(token: str, *args, **kwargs) -> Any:
            if token in token_list:
                return func(token=token, *args, **kwargs)
            raise Exception('Wrong Token')
        return inner
    return deco


@notifier(notifiers=[tg_notifier, sms_notifier, email_notifier])
def my_func():
    print("какая-то логика")


@deco_token(ALLOWED_TOKENS)
@notifier(notifiers=[sms_notifier])
def my_func_2():
    print("какая-то логика my_func_2")


@notifier(notifiers=[sms_notifier, email_notifier])
@deco_token(ALLOWED_TOKENS_2)
def my_func_3(token: str):
    print("какая-то логика my_func_3")


# my_func()
# my_func_2()
# my_func_3("secret token from service three")

# {
#     "func_name": {
#         [
#             {
#                 "params": (),
#                 "timestamp": "2233132312",
#                 "value": 123
#             }
#         ]
#     }
# }


def show_message_before_function_deco(msg: str):
    def decorator(some_func: Callable):
        print("Декорируем функцию", some_func)

        @wraps(some_func)
        def inner_func(*args, **kwargs):
            print(msg)
            return some_func(*args, **kwargs)
        return inner_func
    return decorator


@show_message_before_function_deco(msg="задекорировали класс")
class SimpleClass:
    @time_it
    def __call__(self, *args, **kwargs):
        print("вызываю объект класса")

    @staticmethod
    def sample():
        pass


print(SimpleClass)
my_obj = SimpleClass()
my_obj()
