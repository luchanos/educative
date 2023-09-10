from functools import wraps
from typing import Callable, Any
import logging


# 3.2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в
# случае успешного выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так,
# чтобы выполнение функции было повторено ещё раз с теми же самыми аргументами, но не более 10 раз.
# Если после последней попытки функцию так и не удастся выполнить успешно, то бросать исключение.
def retry(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        attempts = 10
        while True:
            try:
                return func(*args, **kwargs)
            except Exception as err:
                logging.error(f"Error: {err}")
                if attempts == 0:
                    raise
                attempts -= 1
    return inner


# 3.2.2 Параметризовать декоратор таким образом, чтобы количество попыток выполнения функции можно было задавать как
# параметр во время декорирования.
def retry_parametrized(attempts: int) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            nonlocal attempts
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    logging.error(f"Error: {err}")
                    if attempts == 0:
                        raise
                    attempts -= 1
        return inner
    return outer
