CNT = 0


def function_1():
    global CNT
    CNT = 100
    print("Запуск функции function_1")
    print("Значение переменной CNT", CNT)
    CNT += 1


def function_2():
    global CNT
    CNT = 101
    print("Запуск функции function_2")
    print("Значение переменной CNT", CNT)
    CNT += 1


def function_3():
    global CNT
    CNT = 102
    print("Запуск функции function_3")
    print("Значение переменной CNT", CNT)
    CNT += 1


# function_1()
# function_2()
# function_3()
# print("Значение переменной CNT в глобальном скоупе", CNT)


def func_print_message(msg):
    print("Печатаю сообщение!", msg)
    return msg * 10


def print_advertisement():
    print("Покупайте наших котиков!")


def func_executor(some_func, *args, **kwargs):
    print("Отправка метрики на запуск какой-то там функции")
    return some_func(*args, **kwargs)


# def some_function(arg_for_print_in_inner_func):
#     print("Запускаю функцию some_function")
#
#     def inner_function(func_param, *args, **kwargs):
#         print("Аргумент, который был передан в some_function и напечатан в inner_function", arg_for_print_in_inner_func)
#         print("Внутренняя функция inner_func")
#         result_from_func_param = func_param(*args, **kwargs)
#         return result_from_func_param, arg_for_print_in_inner_func * 100
#
#     return inner_function


# result_from_some_function = some_function()
# print(result_from_some_function)
# result_from_some_function()

# for num in range(10):
#     function_to_be_called = some_function(num)
#     print(function_to_be_called)
#     print(function_to_be_called(print_advertisement))
#     print(function_to_be_called(func_print_message, "test"))


def our_first_shiny_decorator(func_param):
    print("Запускаю функцию some_function")

    def inner_function(*args, **kwargs):
        print("Информационное сообщение")
        result_from_func_param = func_param(*args, **kwargs)
        return result_from_func_param

    return inner_function


func_advertisement_decorated = our_first_shiny_decorator(print_advertisement)
print(func_advertisement_decorated())

func_print_message_decorated = our_first_shiny_decorator(func_print_message)
print(func_print_message_decorated("test"))

func_advertisement_decorated()
func_advertisement_decorated()
func_advertisement_decorated()

result = func_print_message_decorated("TEST")
print(func_print_message_decorated("test"))
print(func_print_message_decorated("AAAAA"))
