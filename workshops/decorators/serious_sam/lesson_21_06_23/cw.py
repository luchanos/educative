# def function():
#     return 123


# def another_sample_func(variable):
#     print(variable)
#     return variable()

# def another_sample_func(variable):
#     print(variable)
#     return variable

# print(another_sample_func(function)())

def func():
    c = 1
    def func_in_func():
        c = 1
        print(456)
        return 123
    c = 1
    return func_in_func


c = 1
# print(func()())

# cnt = 0
#
#
# def simple_func():
#     cnt = 1234
#     global cnt
#     print(cnt)
#     cnt = cnt + 1
#
#
# simple_func()
# simple_func()
# simple_func()
# simple_func()
# print(cnt)
# print(cnt)
# print(cnt)

# print(cnt := simple_func(cnt))
# print(cnt := simple_func(cnt))
# print(cnt := simple_func(cnt))
# print(cnt := simple_func(cnt))

# cnt = simple_func(cnt)
# print(cnt)
# cnt = simple_func(cnt)
# print(cnt)
# cnt = simple_func(cnt)
# print(cnt)
# cnt = simple_func(cnt)
# print(cnt)


def function():
    return 123


def one_more_func():
    return 456


# def messager(func):
#     print("Тестовое сообщение")
#     return func()


# print(messager(function))

def summarizer(a, b):
    return a + b


def messager(func):
    def another_func(*args, **kwargs):
        print("Тестовое сообщение")
        return func(*args, **kwargs)
    return another_func


function_123_decorated = messager(function)
function_one_more_func_decorated = messager(one_more_func)
summarizer_decorated = messager(summarizer)
print(function_123_decorated)
print(function_123_decorated())
print(function_one_more_func_decorated())
print(summarizer_decorated(a=1, b=2))
# print(function_123_decorated())
# print(function_123_decorated())
# print(function_123_decorated())
# print(function_123_decorated())
# print(function_123_decorated())
