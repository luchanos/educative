from functools import wraps
from time import sleep, time
from typing import Callable, Any


# 4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран.
# 4.2 Доработать декоратор таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения.
def time_it(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        start = time()
        result = func(*args, **kwargs)
        print(f"Время выполнения задекорированной функции {func.__name__}: {time() - start}")
        return result
    return inner


# 4.3 Доработать декоратор так, чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать
# во время декорирования, как параметр.
def time_it_to_file(filename: str) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            start = time()
            result = func(*args, **kwargs)
            log_msg = f"Время выполнения задекорированной функции {func.__name__}: {time() - start}"
            print(log_msg)
            with open(filename, "a") as file_object:
                file_object.write(f"{log_msg}\n")
            return result
        return inner
    return outer


@time_it_to_file("log.txt")
def func_to_be_decorated():
    sleep(1)


if __name__ == "__main__":
    func_to_be_decorated()
