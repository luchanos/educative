from typing import Callable


# def messager(text: str = "TEXT"):
#     def outer(func: Callable) -> Callable:
#         def inner(*args, **kwargs):
#             print(text)
#             return func(*args, **kwargs)
#         return inner
#     return outer


# def messager_2(func: Callable) -> Callable:
#     def another_func(*args, **kwargs):
#         print("Какая-то логика до вызова функции")
#         result = func(*args, **kwargs)
#         print("Какая-то логика после вызова вызова функции")
#         return result
#     return another_func

# def summarizer(a, b):
#     return a + b
#
#
# summarizer_new = messager(summarizer, "Sample Text")
# print(summarizer_new(1, 2))

# @messager(text="Sample Text")
# def summarizer(a, b):
#     return a + b
#
#
# @messager()
# def summarizer_2(a, b, c):
#     return a + b + c
#
#
# @messager("123")
# def summarizer_3(a, b, c):
#     return a + b + c
#
#
# @messager("456")
# def summarizer_4(a, b, c):
#     return a + b + c
#
#
# @messager("dfgbdfgb")
# def summarizer_5(a, b, c):
#     return a + b + c
#
#
# print(summarizer(1, 2))
# print(summarizer_2(1, 2, 3))
# print(summarizer_3(1, 2, 3))
# print(summarizer_4(1, 2, 3))
# print(summarizer_5(1, 2, 3))


def messager(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("Sample Text")
        return func(*args, **kwargs)
    return inner


def messager_2(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("ABC")
        return func(*args, **kwargs)
    return inner


@messager_2
@messager
def summarizer(a, b):
    return a + b


print(summarizer(1, 2))
