from typing import Union


def summarizer(num_1: int, num_2: int, *args, **kwargs) -> int:
    return num_1 + num_2 + sum(args) + sum(kwargs.values())


def simple_calculator(num_1: Union[float, int],
                      num_2: Union[float, int],
                      operation: str,
                      cast_to_int: bool = False,
                      *args,
                      **kwargs) -> Union[float, int]:
    result = None
    if operation == "/":
        result = num_1 / num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "+":
        result = summarizer(num_1=num_1, num_2=num_2)
    elif operation == "-":
        result = num_1 - num_2
    else:
        print("Операция некорректна")
    return int(result) if cast_to_int is True else result


# print(simple_calculator(1, 2, "/"))  # позиционная передача аргументов

# a, b, c = 1, 2, 3
# print(a, b, c)

# print(simple_calculator(num_2=1, num_1=2, operation="/"))  # передача аргументов по ключу

# print(simple_calculator(1, 2, 3, 4, 5, 6))
# print(simple_calculator(num_2=1, num_1=2, operation="/"))

# print(simple_calculator(1, 2, num_1=2, operation="/"))


# print(summarizer(1, 2, 3, 4, 5, 6, 7))
# print(summarizer(1, 2, 3, 4, 5, 6))
# print(summarizer(1, 2, 3, 4, 5))
# print(summarizer(1, 2, 3))
# print(summarizer(1, 2))

# print(summarizer(1, 2, 3, 3, 3, num_3=3, num_4=4, num_5=5))

# print(simple_calculator(num_1=5, num_2=3, operation="/"))
# print(simple_calculator(num_1=5, num_2=3, operation="/", cast_to_int=True))

# print(1 == True)
# print(1 + True)
# print(True - 2)
# print(True + True + True + 1 - 10 - False)
# print(bool(1))
# print(bool(0))
# print(bool(""))
# print(bool([]))
# print(bool("123"))
# print(bool([1, 2]))
# print(1 in [True, False])
# print({True, 1, 0, False})

params_tuple_1 = (1, 2, "/")
params_tuple_2 = (1, 2, "/", True)

params_dict_1 = {
    "num_1": 10,
    "num_2": 2,
}

# print(simple_calculator(*params_tuple_1))
# print(simple_calculator(*params_tuple_2))
print(simple_calculator(**params_dict_1))
