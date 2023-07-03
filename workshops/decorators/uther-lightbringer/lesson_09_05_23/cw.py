# def func_0():
#     print("Вызывается функция func_0")
#
#     def inner_func():
#         print("вызов inner_func")
#         return 1234
#
#     return inner_func
from typing import Callable


# print(func_0)
# print(func_0())

def simple_func():
    print("Какая-то функция")
    return "РЕЗУЛЬТАТ simple_func"


# def func_0(some_func: Callable):
#     print("Вызывается функция func_0")
#     some_var = 1
#
#     some_func()
#
#     def inner_func():
#         print("вызов inner_func")
#         print(some_var)
#         print(some_func())
#         return 1234
#
#     return inner_func

# "Покупайте наших котиков"
# нужно написать "штуку", которая бы принимала на вход какую-то функцию (f1), и возвращала бы в ответ другую функцию,
# которая бы при вызове себя сначала печатала бы информационное сообщение "покупайте наших котиков", а затем вызывала
# бы внутри себя f1 и возвращала бы её результат.

def f0():
    pass


def f2():
    return 1234


def func_with_param(a, b):
    return a + b


def decorator(f1: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("какая-то логика до вызова целевой функции")
        result = f1(*args, **kwargs)
        sleep(.5)
        print("какая-то логика после вызова целевой функции")
        return result
    return inner


from datetime import datetime
from time import sleep


def time_it(f1: Callable) -> Callable:
    def inner(*args, **kwargs):
        start = datetime.now()
        result = f1(*args, **kwargs)
        print(f"Время работы функции {f1}: {datetime.now() - start}")
        return result
    return inner


@time_it
@decorator
@decorator
@decorator
@decorator
@decorator
@time_it
def func_with_param_1(a, b):
    sleep(1)
    return a + b


# f0_new = decorator(f0)
# f2_new = decorator(f2)
# print(f0_new)
# print(f2_new)
# print(f0_new())
# print(f2_new())
# func_with_param_new = decorator(func_with_param)
# print(func_with_param_new)
# print(func_with_param_new(1, b=2))

sleep(1)
print(func_with_param_1)
print(func_with_param_1(1, 2))
