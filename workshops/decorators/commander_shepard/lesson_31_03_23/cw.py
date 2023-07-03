from typing import Callable, Final

from workshops.decorators.commander_shepard.lesson_17_03_23.cw import get_in
from workshops.decorators.commander_shepard.lesson_24_03_23.cw import printer, clean_list, sample_list


def func_call_another_func(some_func: Callable, arg_for_some_func, *args, **kwargs):
    print("#" * 100)
    result = some_func(*args, **kwargs)
    print(f"Результат функции {some_func}: {result}")
    print(f"Аргумент для самой функции: ", arg_for_some_func)
    return result


# print(func_call_another_func(get_in, 1))
# print(func_call_another_func(printer, 1, 2, 3, 4, 5, 6, 7, 8, additional_keyword_argument=9, a=1, b=2, c=3))
# print(func_call_another_func(clean_list, sample_list))

# print(sample_list)

CNT = 0


def function_1():
    a = 1
    global CNT
    CNT += 1
    print("Запуск функции function_1")
    print("Значение переменной CNT", CNT)


def function_2():
    global CNT
    CNT += 1
    print("Запуск функции function_2")
    print("Значение переменной CNT", CNT)


def function_3():
    global CNT
    CNT += 1
    print("Запуск функции function_3")
    print("Значение переменной CNT", CNT)


# function_1()
# function_2()
# function_3()
# print(CNT)


# def func_print_message(msg):
#     print("Печатаю сообщение!", msg)
#     return msg * 10


def print_advertisement():
    print("Покупайте наших котиков!")
    return 1


def func_executor(some_func: Callable, *args, **kwargs):
    print("Отправка метрики на запуск какой-то там функции")
    return some_func(*args, **kwargs)


# print(func_executor(print_advertisement))
# print(func_executor(func_print_message, "A"))


def metrics_decorator(func_to_be_called: Callable) -> Callable:
    def inner_function(*args, **kwargs):
        print("Отправка метрики на запуск какой-то там функции")
        return func_to_be_called(*args, **kwargs)
    return inner_function


@metrics_decorator
def func_print_message(msg):
    print("Печатаю сообщение!", msg)
    return msg * 10


@metrics_decorator
def print_advertisement():
    print("Покупайте наших котиков!")
    return 1


# new_func_print_message = metrics_decorator(func_print_message)
# print(new_func_print_message("сообщение"))
# new_print_adv = metrics_decorator(print_advertisement)
# new_print_adv()
# print(new_func_print_message)
# print(func_print_message)

print(func_print_message, print_advertisement)


def outer(msg, b, *args, **kwargs):
    def inner(a):
        print(args, kwargs)
        print(msg, a, b)
        return b()

    return inner


for i, func in enumerate([sum, print, list, tuple, lambda x: None]):
    print(outer(i, func))
