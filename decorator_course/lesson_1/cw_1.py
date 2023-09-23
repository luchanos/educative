# a = 1
# b = a
# c = a
# d = b

# print(a, b, c, d)

# print()
# print
# e = print
# e(a, b, c, d)
# print(a, b, c, d)

# print = 123
# print(a, b, c, d)

# print(id(None))
# print(print(1, 2, 3, 4))

# print(print)

# e = print
# e(1, 2, 3)

# def my_func(a, b, c, d, e):
#     return a / b * c + d - e
#
#
# res = my_func(1, 2, 3, 4, 5)
# print(res)


# def summarizer(aaa, b=123, *, a=0, c=0, d=0, e=0):
#     print(a, c, d, e)
#     return a + b + c + d + e


# def summarizer(a, b=0, k=100, *args, **kwargs):
#     print(a, b, k, args, kwargs)
#     num_list = [a, b, k]
#     num_list += args
#     for el in kwargs.values():
#         num_list.append(el)
#     print(num_list)
#     return {"name": "Nikolai", "checksum": sum(num_list)}
#
#
# params_dict = {
#     "n": 123,
#     "m": 123
# }
# params_tuple = (1, 2, 3, 4, 5, 6)
#
# result1 = summarizer(1, 2, *params_tuple, l=100, **params_dict)
# print(result1)

from typing import Any, Callable


# def func():
#     return 1
#
#
# def my_func(some_function: Callable) -> Callable:
#     a = 1
#     b = 2
#     c = 3
#
#     def func_2():
#         return 2
#
#     print(some_function())
#     print(func_2)
#     return func_2
#
#
# resulted_func = my_func(func)
# print(resulted_func)


# a = 1
#
#
# def my_func():
#     global a
#     a += 123
#     print(a)
#
#
# my_func()
# print(a)


# def my_func(b):
#     def inner(a, b, c):
#         nonlocal b
#         b += 234
#         print(b)
#
#     inner(4, 5, 6)
#     print(b)
#
#
# my_func(1)


# def my_func():
#     return 123
#
#
# def summarizer(a, b):
#     return a + b


def decorator(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        print("Before")
        res = func(*args, **kwargs)
        print("After")
        return res
    return inner


# new_func = decorator(my_func)
# print(new_func)
# print(new_func())
#
# new_summarizer = decorator(summarizer)
# print(new_summarizer)
# print(new_summarizer(1, 2))

from datetime import datetime
from time import sleep


def time_it(func: Callable) -> Callable:
    @wraps(func)
    def inner_time_it(*args, **kwargs) -> Any:
        start = datetime.now()
        res = func(*args, **kwargs)
        print(f"{func}:", datetime.now() - start)
        return res
    return inner_time_it


def buy_cats(func: Callable) -> Callable:
    def inner_buy_cats(*args, **kwargs) -> Any:
        sleep(4)
        print("Buy cats!")
        res = func(*args, **kwargs)
        return res
    return inner_buy_cats

c = 1


# @buy_cats
# @buy_cats
# @buy_cats
# @buy_cats
# @time_it
# @buy_cats
# def my_func():
#     sleep(1)
#     return 123


# @time_it
# def summarizer(a, b):
#     sleep(3)
#     return a + b


# print(my_func, summarizer)
# print(my_func())
# print(summarizer(1, 2))


from functools import wraps


def buy_cats_parametrized(msg):
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner_buy_cats(*args, **kwargs) -> Any:
            print(msg)
            res = func(*args, **kwargs)
            return res
        return inner_buy_cats
    return outer


c = 1
@time_it
@buy_cats_parametrized("sample_text")
@time_it
def my_func():
    return 123


print(my_func)

# new_my_func = buy_cats_parametrized(my_func, "sample text")
# print(new_my_func())
