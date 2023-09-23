from datetime import datetime
from functools import wraps


def log_to_file(file_path):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            timestamp = datetime.now()
            with open(file_path, "a") as f_o:
                f_o.write(f"{timestamp}: {func.__name__}, result: {res}\n")
            return res
        return inner
    return outer


# @log_to_file("log.txt")
# def my_func(a, b):
#     return a + b
#
#
# @log_to_file("log.txt")
# def not_my_func():
#     return "test"
#
#
# my_func(1, 2)
# not_my_func()


from random import randint


# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as err:
#             print("Error:", err)
#     return inner
#
#
# @decorator
# def throw_exc(a, b):
#     if randint(0, 4) != 3:
#         raise Exception("sample error")


# throw_exc(1, 2)


from random import randint


def retry(attempts):
    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal attempts
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    print("Error:", err)
                    attempts -= 1
                    if attempts == 0:
                        raise err
        return inner
    return outer


@retry(attempts=10)
def raise_error(a, b):
    if randint(0, 3) != 2:
        raise TimeoutError("Timeout")
    return a + b


raise_error(1, 2)















