from functools import wraps
from typing import Callable, Any


def retry(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        total_attempts = 5
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as err:
                total_attempts -= 1
                print("Error:", err, "| Total attempts left:", total_attempts)
                if total_attempts == 0:
                    raise
    return inner


def supress_error(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        try:
            return func(*args, **kwargs)
        except Exception:
            pass
    return inner


# @supress_error
# @retry
# def divisor(a, b):
#     return a / b


SECRET_PASSWORD = "SECRET_PASSWORD"


def password_checker(password: str) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            if password == SECRET_PASSWORD:
                return func(*args, **kwargs)
            raise Exception("Password is not valid!")
        return inner
    return outer


# @password_checker("secret")
# class SimpleClass:
#     pass


# class AnotherClass(SimpleClass):
#     pass


# some_object = AnotherClass()

class_mapper = {
}


def outer(something: Callable) -> Callable:
    @wraps(something)
    def inner(*args, **kwargs) -> Any:
        some_object = something(*args, **kwargs)
        if something.__name__ in class_mapper:
            class_mapper[something.__name__] += 1
        else:
            class_mapper[something.__name__] = 0
        return some_object
    return inner


@outer
class SimpleClass:
    pass


@outer
class SimpleClass2:
    pass


# o = SimpleClass()
# SimpleClass()
# SimpleClass()
# SimpleClass2()
# SimpleClass2()
# SimpleClass2()
#
# print(class_mapper)


def notifier(list_of_notifiers: list) -> Callable:
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            result = func(*args, **kwargs)
            for notifier in list_of_notifiers:
                notifier(result)
            return result
        return inner
    return outer


class TGNotifier:
    def __call__(self, result, *args, **kwargs):
        print("Send to telegram", result)


class EmailNotifier:
    def __init__(self, address):
        self.address = address

    def __call__(self, result, *args, **kwargs):
        print("Send to email", self.address, result)


class SmsNotifier:
    def __call__(self, result, *args, **kwargs):
        print("Send by sms", result)


class PushNotifier:
    def __call__(self, result, *args, **kwargs):
        print("Send push", result)


@notifier(
    [
        TGNotifier(),
        SmsNotifier(),
        EmailNotifier("lol@kek.com"),
        PushNotifier()
    ]
)
def divisor(a, b):
    return a / b


@notifier(
    [
        TGNotifier(),
        EmailNotifier("kek@kek.com"),
    ]
)
def summarizer(a, b):
    return a + b


print(divisor(1, 1))
print(summarizer(1, 1))
