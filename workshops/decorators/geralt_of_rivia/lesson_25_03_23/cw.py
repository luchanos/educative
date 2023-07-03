from typing import Callable

CNT = 0


def function_1():
    global CNT
    CNT = 1
    print("Значение счетчика, вызываемое из function_1:", CNT)
    CNT += 1


def function_2():
    global CNT
    CNT = 2
    print("Значение счетчика, вызываемое из function_2:", CNT)
    CNT += 1


def function_3():
    global CNT
    CNT = 3
    print("Значение счетчика, вызываемое из function_3:", CNT)
    CNT += 1


def function_with_another_function_declaration(message: str) -> Callable:
    print("Это функция, которая объявляет внутри себя другую функцию")
    CNT = "Это CNT из scope function_with_another_function_declaration"

    def inner_func():
        global CNT
        print(message)
        print("Значение CNT:", CNT)
        print("Это функция, которая была объявлена внутри другой функции")

    print("Вывод функции inner_func внутри function_with_another_function_declaration:", inner_func)
    return inner_func


# function_1()
# function_2()
# function_3()
# print(f"Функции запустились в сумме {CNT} раз")


# for _ in range(10):
#     function_with_another_function_declaration()

# function_with_another_function_declaration("Сообщение")()
#
# for num in range(10):
#     func = function_with_another_function_declaration(str(num))
#     print("Вывод функции inner_func полученной от function_with_another_function_declaration:", func)
#     func()


def outer_func(outer_param):
    print("outer_func call")

    def inner_func(inner_param):
        print("inner_func call")
        print("parameter from outer_func scope", outer_param)
        print("parameter from inner_func scope", inner_param)
        return inner_param * 10

    return inner_func


# print(outer_func(123)(456))


def metric_deco(some_func: Callable):
    print("Декорируем функцию", some_func)

    def inner_func(*args, **kwargs):
        print("inner_func call")
        result = some_func(*args, **kwargs)
        return result

    return inner_func


def simple_func(param_1, param_2):
    print("Вызов simple_func с параметрами:", param_1, param_2)
    return f"Результат работы simple_func с параметрами: {param_1}, {param_2}"


simple_func_decorated = metric_deco(simple_func)
function_1_decorated = metric_deco(function_1)
function_2_decorated = metric_deco(function_2)
function_3_decorated = metric_deco(function_3)
print(simple_func_decorated, function_1_decorated, function_2_decorated, function_3_decorated)
simple_func_decorated(1, 2)
function_1_decorated()
function_2_decorated()
function_3_decorated()
