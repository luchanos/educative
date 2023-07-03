from abc import ABC, abstractmethod
from dataclasses import dataclass
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


def send_to_tg(admin_chat_id: int, res: str):
    requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                 f"chat_id={admin_chat_id}&text={res}-TG")


def send_to_email(admin_chat_id: int, res: str):
    requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                 f"chat_id={admin_chat_id}&text={res}-EMAIL")


def send_to_sms(admin_chat_id: int, res: str):
    requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                 f"chat_id={admin_chat_id}&text={res}-SMS")


class Recipient:
    def __init__(self, tg_id=None, phone_number=None, email=None):
        self.tg_id = tg_id
        self.phone_number = phone_number
        self.email = email


class BaseNotifier(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs):
        pass


class TgNotifier(BaseNotifier):
    def __init__(self, token):
        self.token = token

    def __call__(self, recipient: Recipient, res: Any, *args, **kwargs):
        requests.get(f"https://api.telegram.org/bot{self.token}/SendMessage?"
                     f"chat_id={recipient.tg_id}&text={res}-TG")


class EmailNotifier(BaseNotifier):
    def check_token(self):
        print("Проверка токена на ликвидность или его получение")

    def __call__(self, recipient: Recipient, res: Any, *args, **kwargs):
        self.check_token()
        requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                     f"chat_id={recipient.tg_id}&text={res}-EMAIL-{recipient.email}")


class SmsNotifier(BaseNotifier):
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def __call__(self, recipient: Recipient, res: Any, *args, **kwargs):
        requests.get(f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?"
                     f"chat_id={recipient.tg_id}&text={res}-SMS-api-key{self.api_key}-base-url{self.base_url}")


def notifier(recipients_list: list[Recipient], notifiers_tuple: tuple):
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            for recipient in recipients_list:
                for notifier_object in notifiers_tuple:
                    notifier_object(recipient=recipient, res=res)
            return res
        return inner
    return outer


@counter_deco
@time_it
@decorator(custom_message="test")
@notifier(recipients_list=[150117822, 440284906, 164549711, 362857450], notifiers_tuple=(send_to_tg, ))
def func_print_message(msg):
    sleep(.2)
    print("Печатаю сообщение!", msg)
    return msg * 10


@notifier(recipients_list=[
    Recipient(email="lol@kek.ru", phone_number=123, tg_id=164549711),
    Recipient(email="lol@kek.ru", phone_number=123, tg_id=253163342),
    Recipient(email="lol@kek.ru", phone_number=123, tg_id=383712412),
    Recipient(email="lol@kek.ru", phone_number=123, tg_id=362857450),
                           ],
          notifiers_tuple=(
                  TgNotifier(token="6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
                  TgNotifier(token="6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
                  SmsNotifier(api_key="123", base_url="ws://192.182.32.11"),
                  EmailNotifier()
          )
          )
@counter_deco
def simple_func():
    return 1000


# print(func_print_message)
# print(func_print_message("123"))
# simple_func()
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


def passworder(password):
    def class_deco(cls):
        def inner(secret_password: str, *args, **kwargs):
            if password != secret_password:
                raise Exception
            return cls(*args, **kwargs)
        return inner
    return class_deco


@passworder(password="secret_password")
class MyClass:
    pass


print(MyClass)
res = MyClass(secret_password="secret_password")
print(res)
