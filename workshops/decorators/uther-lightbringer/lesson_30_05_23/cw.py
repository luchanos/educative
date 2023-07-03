from typing import Callable
import requests


def logging(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"result of funcion {func}: {result}")
        return result
    return inner


def logging_to_file(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("logfile.txt", "a") as f_o:
            f_o.write(f"{result}\n")
        print(f"result of funcion {func}: {result}")
        return result
    return inner


def logging_to_telegram(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        URL = f"https://api.telegram.org/bot6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10/SendMessage?chat_id=362857450&text={result}"
        requests.post(URL)
        print(f"result of funcion {func}: {result}")
        return result
    return inner


# @logging_to_telegram
# @logging_to_file
# @logging
# def summarizer(a, b):
#     return a + b


# print(summarizer(1, 2))


class TerminalNotifier:
    def __call__(self, result):
        print(result)


class FileNotifier:
    def __init__(self, filename: str):
        self.filename = filename

    def __call__(self, result):
        with open(self.filename, "a") as f_o:
            f_o.write(f"{result}\n")


class TgNotifier:
    def __init__(self, token: str):
        self.token = token

    def __call__(self, result):
        url = f"https://api.telegram.org/bot{self.token}/SendMessage?chat_id=362857450&text={result}"
        requests.post(url)


def notifier(notifiers_list):
    def outer(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            for notifier in notifiers_list:
                notifier(result)
            return result
        return inner
    return outer


@notifier(
    [
        TerminalNotifier(),
        FileNotifier("notify.txt"),
        TgNotifier("6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
        TgNotifier("6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
        TgNotifier("6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
        TgNotifier("6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10"),
    ]
)
def summarizer(a, b):
    return a + b


@notifier(
    [
        TerminalNotifier(),
        TgNotifier("6230160478:AAGNvGhQ-AwrKjwv_mXs-5qDZjzRxT-xT10")
    ]
)
def multiplier(a, b):
    return a * b


print("result of summarizer", summarizer(1, 2))
print("result of multiplier", multiplier(1, 2))


def supress_errors(exc_tuple):
    def outer(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(f"result of funcion {func}: {result}")
                return result
            except exc_tuple:
                print("была ошибка, но я её подавил")
        return inner
    return outer


@supress_errors(
    (
        ZeroDivisionError,
        KeyError
    )
)
def division(a, b):
    return a / b


print(division(1, 2))
print(division(3, 0))
