from datetime import datetime
from functools import reduce
from typing import Callable


def outer(var):
    def inner():
        nonlocal var
        print(var)
        var += 1
    inner()
    print(var)


def time_it(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        finish = datetime.now()
        print(f"Время работы функции {func}: {finish - start}")
        return result
    return inner


def logging_to_file(path_to_log: str) -> Callable:
    def wrapper(func: Callable) -> Callable:
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"Результат функции {func}: {result}")
            with open(path_to_log, "a") as f_o:
                f_o.write(f"{result}\n")
            return result
        return inner
    return wrapper


# @logging_to_file
@time_it
def summarizer(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


@logging_to_file(path_to_log="mult_log.txt")
@time_it
def multiplier(*args, **kwargs):
    # return reduce(lambda a, b: a * b, [*args, *kwargs.values()])
    result = 1
    for el in [*args, *kwargs.values()]:
        result *= el
    return result


# print(summarizer(1, 1, 1, 1, 1, c=1, e=1, ))
# new_summarizer = logging_to_file(summarizer, "sum_log.txt")
# new_multiplier = logging_to_file(multiplier, "mult_log.txt")
# print(new_multiplier(1, 1, 1, 1, 1, c=2, e=3))
# print(new_summarizer(1, 1, 1, 1, 1, c=2, e=3))
# print(multiplier(1, 1, 1, 1, 1, c=2, e=3))

try:
    1 / 0
except ZeroDivisionError as err:
    print("перехвачена ошибка!", err)
    raise
print("Программа завершена")
