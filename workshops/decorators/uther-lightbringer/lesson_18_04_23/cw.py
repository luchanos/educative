from random import randint
from typing import Union


# print("Информационное сообщение 1")
# print("Информационное сообщение 2")
# print("Информационное сообщение 3")
# print("Информационное сообщение 4")


def print_info_messages():
    print("Информационное сообщение 1")
    print("Информационное сообщение 2")
    print("Информационное сообщение 3")
    print("Информационное сообщение 4")
    if randint(0, 10) % 2 == 0:
        return "Функция завершила свою работу"
    print("return под if не сработал")


# print_info_messages = 123
# print(print_info_messages)
# result = print_info_messages()
# print(result)

# print(print_info_messages)
# for _ in range(10):
#     print(print_info_messages())

# print = "123"
# print(sum([1, 2, 3]))
# sum = 123
# list = [1, 2, 3]
# list((1, 2, 3))


# def summarizer():
#     return sum([1, 2, 3])
#
#
# print(summarizer())


def simple_calculator(num_1: Union[float, int], num_2: Union[float, int], operation: str) -> Union[float, int]:
    if operation == "/":
        return num_1 / num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    print("Операция некорректна")


print(simple_calculator(1, 2, "/"))
print(simple_calculator(num_2=1, num_1=2, operation="/"))
