from functools import partial, wraps
from typing import Callable, Any
from datetime import datetime
from time import sleep


def messager(msg: str) -> Callable:
    def wrapper_1(func: Callable) -> Callable:
        c = 1

        @wraps(func)
        def inner_msg_1(*args, **kwargs):
            sleep(2)
            print(msg)
            return func(*args, **kwargs)
        return inner_msg_1
    return wrapper_1


def messager_2(msg: str) -> Callable:
    c = 1
    def wrapper(func: Callable) -> Callable:
        c = 1

        @wraps(func)
        def inner_msg_2(*args, **kwargs):
            sleep(2)
            print(msg)
            return func(*args, **kwargs)
        return inner_msg_2
    return wrapper


def time_it(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print("TIME:", datetime.now() - start)
        return result
    return inner


@messager_2("Example")  # wrapper
@time_it
@messager("123")  # wrapper_1
def summarizer(a, b):
    return a + b


@messager_2("Example")  # wrapper
@time_it
@messager("123")  # wrapper_1
def summarizer_2(a, b):
    return a + b


print(summarizer_2)
# print(summarizer(1, 2))

# par_1 = partial(summarizer, a=1)
# par_1()
