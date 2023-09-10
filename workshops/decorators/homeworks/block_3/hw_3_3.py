from functools import wraps
from time import time, sleep
from typing import Callable, Any


# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции.
def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        params_tuple = args + tuple(sorted(kwargs.items()))
        if params_tuple not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[params_tuple] = result
            return result
        else:
            return cache_dict[params_tuple]
    return inner


# 3.2 Сделать так, чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической
# очистки кэша в процессе выполнения функций.
def cache_with_timer(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        expiry_time = 2
        params_tuple = args + tuple(sorted(kwargs.items()))
        if params_tuple not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[params_tuple] = {"result": result, "time": time()}
            return result
        else:
            if time() - cache_dict[params_tuple]["time"] > expiry_time:
                result = func(*args, **kwargs)
                cache_dict[params_tuple]["result"] = result
                cache_dict[params_tuple]["time"] = time()
            return cache_dict[params_tuple]["result"]
    return inner


def cache_with_timer_autoclean_cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        expiry_time = 2
        for params_key in list(cache_dict.keys()):
            if time() - cache_dict[params_key]["time"] > expiry_time:
                del(cache_dict[params_key])

        params_tuple = args + tuple(sorted(kwargs.items()))
        if params_tuple not in cache_dict:
            result = func(*args, **kwargs)
            cache_dict[params_tuple] = {"result": result, "time": time()}
            return result
        else:
            return cache_dict[params_tuple]["result"]
    return inner


def cache_with_timer_autoclean_cache_parametrized(expiry_time: int):
    def outer(func: Callable) -> Callable:
        cache_dict = {}

        @wraps(func)
        def inner(*args, **kwargs) -> Any:
            for params_key in list(cache_dict.keys()):
                if time() - cache_dict[params_key]["time"] > expiry_time:
                    del(cache_dict[params_key])

            params_tuple = args + tuple(sorted(kwargs.items()))
            if params_tuple not in cache_dict:
                result = func(*args, **kwargs)
                cache_dict[params_tuple] = {"result": result, "time": time()}
                return result
            else:
                return cache_dict[params_tuple]["result"]
        return inner
    return outer


@cache_with_timer_autoclean_cache_parametrized(5)
def func_to_be_decorated(a: Any, b: Any) -> Any:
    sleep(5)
    return a + b


if __name__ == "__main__":
    for _ in range(10):
        print(func_to_be_decorated(1, 2))
    wait_period = 3
    print(f"Wait {wait_period} seconds")
    sleep(wait_period)
    for _ in range(10):
        print(func_to_be_decorated(1, 2))
