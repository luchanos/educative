from typing import Callable, Any
from datetime import datetime
from time import sleep


def metric_deco_simple(some_func: Callable):
    print("Декорируем функцию", some_func)

    def inner_func(*args, **kwargs):
        print("Отправка метрик или какое-то информационное сообщение")
        result = some_func(*args, **kwargs)
        print("Логика после вызова декорируемой функции")
        return result

    return inner_func


@metric_deco_simple
def simple_func(param_1, param_2):
    print("Вызов simple_func с параметрами:", param_1, param_2)
    return f"Результат работы simple_func с параметрами: {param_1}, {param_2}"


# simple_func_decorated = metric_deco(simple_func)
# print(simple_func_decorated)
# simple_func_decorated(1, 2)
# print(simple_func)
# simple_func(1, 2)

# CNT = 0
#
#
# def outer_func():
#     CNT = 100
#
#     def inner_func():
#         # global CNT
#         # CNT += 1
#         print(CNT)
#     inner_func()
#
#
# outer_func()
# print(CNT)


# def double_outer_func():
#     nonlocal_cnt = 10
#
#     def outer_func():
#         nonlocal_cnt = 100
#         def inner_func():
#             nonlocal nonlocal_cnt
#             nonlocal_cnt += 1
#             print(50, nonlocal_cnt)
#         inner_func()
#         print(52, nonlocal_cnt)
#
#     print(54, nonlocal_cnt)
#     outer_func()
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


def metric_deco_with_param(info_message: str):
    def metric_deco(some_func: Callable):
        def inner_func(*args, **kwargs):
            nonlocal info_message
            sleep(2)
            info_message = info_message.upper()
            print(info_message)
            return some_func(*args, **kwargs)
        return inner_func
    return metric_deco


@time_it
@metric_deco_with_param(info_message="Какое-то информационное сообщение для первой")
@time_it
def function_1():
    sleep(.1)
    print("function 1")


# @time_it
# @metric_deco_with_param(info_message="Какое-то информационное сообщение для второй")
# def function_2():
#     sleep(.2)
#     print("function 2")


# @time_it
# @metric_deco_with_param(info_message="Какое-то информационное сообщение для третьей")
# def function_3():
#     sleep(.5)
#     print("function 3")


print(function_1)
function_1()


# function_1_decorated = metric_deco(function_1, "Какое-то информационное сообщение для первой")
# function_2_decorated = metric_deco(function_2, "Какое-то информационное сообщение для второй")
# function_3_decorated = metric_deco(function_3, "Какое-то информационное сообщение для третьей")
# function_1_decorated()
# function_2_decorated()
# function_3_decorated()
