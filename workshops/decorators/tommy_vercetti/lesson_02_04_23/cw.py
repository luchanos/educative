from datetime import datetime
from time import sleep
from typing import Callable, Any


def our_first_shiny_decorator(func_param: Callable) -> Callable:
    print("Запускаю функцию some_function")

    def inner_function(*args, **kwargs) -> Any:
        print("Информационное сообщение")
        result_from_func_param = func_param(*args, **kwargs)
        return result_from_func_param

    return inner_function


def func_print_message(msg):
    print("Печатаю сообщение!", msg)
    return msg * 10


def print_advertisement():
    sleep(.5)
    print("Покупайте наших котиков!")


# func_advertisement_decorated = our_first_shiny_decorator(print_advertisement)
# print(func_advertisement_decorated())
#
# func_print_message_decorated = our_first_shiny_decorator(func_print_message)
# print(func_print_message_decorated("test"))


# CNT = 0
#
#
# def outer_func():
#     CNT = 100
#
#     def inner_func():
#         global CNT
#         CNT += 1
#         print(CNT)
#     inner_func()
#
#
# outer_func()
# print(CNT)

# nonlocal_cnt = 0
#
# def double_outer_func():
#     nonlocal_cnt = 10
#
#     def outer_func():
#         nonlocal_cnt = 100
#
#         def inner_func():
#             nonlocal nonlocal_cnt
#             nonlocal_cnt += 1
#             print(nonlocal_cnt)
#
#         inner_func()
#         print(nonlocal_cnt)
#
#     outer_func()
#     print(nonlocal_cnt)
#
#
# double_outer_func()


def time_it(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Any:
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return inner


# print_advertisement_new = time_it(print_advertisement)
# print_advertisement_new()

def calculate_deco(custom_msg: str):
    def metric_deco(func: Callable) -> Callable:
        def func_executor(*args, **kwargs):
            sleep(1)
            print("Сообщение параметризованного декоратора", custom_msg)
            return func(*args, **kwargs)
        return func_executor
    return metric_deco


@time_it
@calculate_deco("test")
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


func_print_message_second(123)
print_advertisement_second()
