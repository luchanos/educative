def func(param_1, param_2, param_3=1, *args, **kwargs):
    c = 1


def f(x, y, *, kx=None, ky=42, **kwargs):
    c = 1


# func(1, 2, key_param_1=10, key_param_2=11)
# f(1, 2, 3, 4, 5, 6, key_param_1=10, key_param_2=11)


CNT = 0


# def func_0(f):
#     print("Вызывается функция func_0")
#     return f()
#
#
# def func_1():
#     global CNT
#     CNT = 100
#     print("Вызывается функция func_1")
#     return 12345
#
#
# print(func_1)
#
# print(CNT)
# print(func_0(func_1))
# print(CNT)


def func_0():
    print("Вызывается функция func_0")

    def inner_func():
        print("вызов inner_func")
        return 1234

    # return inner_func
    return inner_func


print(func_0()())
l = [1, 2, 3, 4]
print(l[0])

inner_func = func_0()
result = inner_func()
print(result)

