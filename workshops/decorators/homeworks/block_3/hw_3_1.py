from functools import wraps
from typing import Callable, Any


# 3.1.1 Написать декоратор, который перед запуском произвольной функции с произвольным набором
# аргументов будет показывать в консоли сообщение "Покупайте наших котиков!" и возвращать результат запущенной функции.
def cat_adviser_deco(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        print("Покупайте наших котиков!")
        return func(*args, **kwargs)
    return inner


# 3.1.2 Параметризовать декоратор таким образом, чтобы сообщение, печатаемое перед выполнением функции можно
# было задавать как параметр во время декорирования.
def cat_adviser_deco_customed(msg: str) -> Callable:
    def outer(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            print(msg)
            return func(*args, **kwargs)
        return inner
    return outer


@cat_adviser_deco
def func_to_be_decorated() -> int:
    return 1


@cat_adviser_deco_customed("Custom message")
def func_to_be_decorated_2() -> int:
    return 1


if __name__ == "__main__":
    print(func_to_be_decorated())
    print(func_to_be_decorated_2())
