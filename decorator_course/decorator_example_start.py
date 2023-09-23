from functools import wraps
from typing import Callable, Any
import logging
from random import randint
from datetime import datetime
from flask import Flask
import telebot
from telebot.types import Message

# flask example
app = Flask("test_app_name")


@app.route("/")
def hello():
    return "123"


app.run()

# telebot example


bot = telebot.TeleBot("")


@bot.message_handler(commands=["start", ])
def simple_handler(message: Message):
    print("Hello")












def retry(attempts: int, exceptions_for_handling: tuple):
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            nonlocal attempts
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions_for_handling as err:
                    attempts -= 1
                    logging.error(f"Error: {err}\nAttempts left: {attempts}")
                    if attempts == 0:
                        raise
        return inner
    return outer


def time_it(func) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Callable:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(f"Work time: {datetime.now() - start}")
        return result
    return inner


def logging_to_file(filepath: str, writing_mode: str = "w") -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filepath, writing_mode) as logfile:
                logfile.write(f"{result}\n")
            return result
        return inner
    return outer


@logging_to_file("logging_random_divider.txt")
@time_it
@retry(attempts=3, exceptions_for_handling=(TypeError, ZeroDivisionError))
def random_divider(low_range: int = 0, high_range: int = 2):
    return randint(low_range, high_range) / randint(low_range, high_range)


print(random_divider())
