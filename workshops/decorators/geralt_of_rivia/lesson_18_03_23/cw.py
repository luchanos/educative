from sys import getsizeof


# def my_func():
#     pass


# print(my_func)
# result = my_func()
# print(getsizeof(result), id(result))

# variable = my_func
# print(my_func)
# print(variable)
# my_func = 100
# print(my_func)
# print(variable)
# print(variable())
# print(my_func())

# print(sum)
# print(sum([1, 2, 3]))
# sum = 100
# print(sum)
# print(sum([1, 2, 3]))

# print(print)
# print(print("123123123"))

# def my_func():
#     return 1
#
#
# print(my_func())

# def calculator(num_1, num_2, operation):
#     if operation == "+":
#         return num_1 + num_2
#     elif operation == "-":
#         return num_1 - num_2
#     elif operation == "*":
#         return num_1 * num_2
#     elif operation == "/":
#         if num_2 == 0:
#             print("Делить на 0 нельзя!")
#             return
#         return num_1 / num_2
#     else:
#         print("Операция некорректна!")


# first = 1
# second = 2
# calc_operation = "/"
# func_args = {
#     "num_1": first,
#     "num_2": second,
#     "operation": calc_operation,
#     "param": 123
# }
# func_args_tuple = (first, second, calc_operation)
# result = calculator(**func_args)
# result = calculator(num_1=first, num_2=second, operation="/", param=123)
# result = calculator(*func_args_tuple)
# func_args_cutted = {
#     "num_2": second,
#     "operation": calc_operation,
# }
# result = calculator(*func_args_tuple[:1], **func_args_cutted)
# print(calculator)
# print(result)


def calculator_with_round_mode(num_1, num_2, operation, cut_to_int=False):
    result = None
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            print("Делить на 0 нельзя!")
            return
        result = num_1 / num_2
    else:
        print("Операция некорректна!")
    return result if not cut_to_int else int(result)


# print(calculator_with_round_mode(3, 2, "/", cut_to_int=True))
# print(calculator_with_round_mode(3, 2, "/"))

def func_print_message():
    print("Печатаю сообщение!", input("введите сообщение: "))


def print_advertisement():
    print("Покупайте наших котиков!")


def func_executor(some_func, *args, **kwargs):
    print("Отправка метрики на запуск какой-то там функции")
    return some_func(*args, **kwargs)


print(func_executor(func_print_message))
print(func_executor(print_advertisement))
print(func_executor(calculator_with_round_mode, 1, 2, "/"))
