# print(1 == True)
# print(0 == True)
# print(0 == False)
from typing import Callable, Any

from workshops.decorators.commander_shepard.lesson_17_03_23.cw import get_in


# print(1 in [True, False])
# print(0 in [True, False])
# print(True in [0, 1])
# print(False in [0, 1])
# print({True, False, 1, 0})
# print(True + False + True - True / True)

# print(bool({1, 2}))
# print(bool([1, 2]))
# print(bool((1, 2)))
# print(bool({}))
# print(bool([]))
# print(bool(()))


# print([1, ] == True)
# print((1, ) == True)
# print({1: 2} == True)


def printer(obligatory_arg_1: Any, obligatory_arg_2: Any, non_obligatory_arg: Any = None, *args, **kwargs):
    print("Обязательный аргумент 1", obligatory_arg_1)
    print("Обязательный аргумент 2", obligatory_arg_2)
    print("Необязательный аргумент", non_obligatory_arg)
    for arg_num, additional_pos_arg in enumerate(args, start=1):
        print(f"Дополнительный позиционный аргумент {arg_num}: {additional_pos_arg}")
    for key, value in kwargs.items():
        print(f"Дополнительный именованный аргумент по ключу {key}: {value}")


# a, b, c, d = [1, 2, 3, 4]
# print(a, b, c, d)

# param_list = [1, 2, 3]
param_dict = {
    "obligatory_arg_2": 2,
    "obligatory_arg_1": 1,
    "non_obligatory_arg": 3
}
# a, b, c = param_dict
# printer(obligatory_arg_1=1, obligatory_arg_2=2, non_obligatory_arg=3)
# printer(1, **param_dict)

# printer(1, 2, 3, 4, 5, 6, 7, 8, additional_keyword_argument=9, a=1, b=2, c=3)
# (1, 2, 3, 4, 5, 6, 7, 8)  - позиционные
# additional_keyword_argument=9, a=1, b=2, c=3 - по имени
# printer(1, 2)

# print = 1
# print(123)
# sum = 1 + 2
# list = []
# l = list()

sample_list = [1, 2, 3]


def clean_list(l: list = None):
    if l is None:
        l = []
    l.clear()


# print(clean_list(sample_list))


def func_call_another_func(some_func: Callable, arg_for_some_func, *args, **kwargs):
    print("#" * 100)
    result = some_func(*args, **kwargs)
    print(f"Результат функции {some_func}: {result}")
    print(f"Аргумент для самой функции: ", arg_for_some_func)
    return result


if __name__ == "__main__":
    print(func_call_another_func(get_in, 1))
    print(func_call_another_func(printer, 1, 2, 3, 4, 5, 6, 7, 8, additional_keyword_argument=9, a=1, b=2, c=3))
    print(func_call_another_func(clean_list, sample_list))

    print(sample_list)
