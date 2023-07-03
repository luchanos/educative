from typing import Union


def calculator(num_1: Union[int, float],
               num_2: Union[int, float],
               operation: str,
               cut_to_int: bool = False) -> Union[int, float, None]:
    result = None
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            print("делить на 0 нельзя")
            return
        result = num_1 / num_2
    else:
        print("Операция некорректна!")
    return result if not cut_to_int else int(result)


num_1_param = 105
num_2_param = 20
operation_param = "/"
# print(calculator)
# print(calculator(num_1_param, num_2_param, "+"))
# print(calculator(num_1=num_1_param, num_2=num_2_param, operation=operation_param))
# param_tuple = (num_1_param, num_2_param, operation_param)
# param_list = [num_1_param, num_2_param, operation_param]
# param_dict = {
#     "num_1": num_1_param,
#     "num_2": num_2_param,
#     "operation": operation_param
# }
# print(calculator(**param_dict))
# for element in param_dict:
#     print(element)

# print(bool(1))
# print(bool(0))
# print(bool([]))
# print(bool([1, ]))
# print(bool(()))
# print(bool((1, )))
# print(bool(""))
# print(bool("123"))

param_list: list = [num_2_param, ]
param_dict = {
    "operation": operation_param
}
param_dict_second = {
    "operation": operation_param,
    "num_2": num_2_param,
    "addition": 123
}

# print(calculator(1, *param_list, **param_dict))
# print(calculator(num_1_param, *param_list, **param_dict, cut_to_int="sdcsdcsdcs"))
print(calculator(num_1=num_1_param, **{"num_2": param_dict_second["num_2"],
                                       "operation": param_dict_second["operation"]}))
# print("" in [0, 1, 2, 3, 4])
# print(1 in [0, 1, 2, 3, 4])
# print(True in [0, 1, 2, 3, 4])
# print(False in [0, 1, 2, 3, 4])
# print(1 == True)
# print(0 == False)
# print(1.0 == True)
# print(0.0 == False)
# print(2 == True)
# print(1 is True)
# print(0 is False)
# print(0 in [True, False, 2, 3])
# print((True + 1 + False + True + True) * "T")

# print(calculator(num_1=num_1_param, num_2=num_2_param, operation=operation_param))


def func_print_message():
    msg = input("введите сообщение: ")
    print("Печатаю сообщение!", msg)


def print_advertisement():
    print("Покупайте наших котиков!")


def func_executor(some_func, *args, **kwargs):
    print("Отправка метрики на запуск какой-то там функции")
    return some_func(*args, **kwargs)


# print(func_executor(func_print_message))
# print(func_executor(print_advertisement))
# print(func_executor(calculator, 1, 2, "/"))

# print([] in [False, 0, 1, 2])
# if not []:
#     print(123)
