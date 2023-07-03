from sys import getsizeof
from typing import Union, Any, Callable

data_dict = {
    "data": {
        "items":
            {
                "users":
                    [
                        {
                            "id": 123
                        },
                        {
                            "id": 456
                        }
                    ]
            }
    }
}


def get_in():
    return 1


# print(get_in())
# another_function = get_in
# get_in = 1234
# print(get_in)
# print(another_function())
# result = get_in()
# print(getsizeof(result), id(result))

# a = 10_000_000
# b = 10_000_000
# c = 10_000_000
# a = b = c = 10_000_000
# print(id(a), id(b), id(c))
# c = 10
# b = 1
# print(a, b, c)
# print(id(a), id(b), id(c))
# some_list = [1, 2, 3]
# another_list = (4, 5, 6, some_list, 7, 8, 9)
# print(another_list)
# some_list[0] = "TEST"
# print(another_list)
# another_list[3][0] = "TESTTEST"
# print(another_list)
# print(some_list)
# print({(), 1, 2, 3, (((([])))), "sdfs"})
# frozenset({(), 1, 2, 3, (((([])))), "sdfs"})
# t = (1, 2, [4, 5])
# t[2] = t[2] + [3, 4]


def calculator(num_1: int, num_2: int, operation: str, cast_to_int: bool = False) -> Union[int, float, None]:
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
            return None
        result = num_1 / num_2
    else:
        print("Операция некорректна!")
    if cast_to_int is True:
        result = int(result)
    return result


# num_1 = 5
# num_2 = 3
# operation = "/"
# print(calculator)
# print(calculator(num_1=num_1, operation=operation, num_2=num_2, cast_to_int=False))
# print(calculator(num_1=num_1, operation=operation, num_2=num_2))
