# print(123)


# def calculator(num_1, *, num_2, operation, round_=False):
#     result = None
#     if operation == "+":
#         result = num_1 + num_2
#     elif operation == "-":
#         result = num_1 - num_2
#     elif operation == "*":
#         result = num_1 * num_2
#     elif operation == "/":
#         result = num_1 / num_2
#     if round_ is True:
#         result = int(result)
#     return result


# print(calculator(3, num_2=10, operation="/", round_=True))
# print(int(1.1))

# l = [0, 1, 2, 3, 4, 5, 6, 7]
# print(False in l)
# print(bool())
# print((True + True + True + True - 100 + True + False) // True)
# print(bool(l))

# print(calculator(10, num_1=3, operation="/", round_=True))

# a = 1
# b = 2
# a, b = b, a
# print(a, b)

# l = [0, 1]
# a, b = l
# print(a, b)

d = {
    "num_1": 10,
    "num_2": 2,
    # "num_3": 2
}
l = [10, 2, 2, 2]

# print(calculator(num_1=d["num_1"], num_2=d["num_1"], operation="/", round_=True))
# print(calculator(*d, operation="+"))
# print(calculator(*l, operation="/", round_=True))

# for el in d:
#     print(el)


def lose_horse():
    print("Lost horse")


def lose_life():
    print("Lost life")


def lose_mind():
    print("Lost mind")


func_dict = {
    "left": lose_horse,
    "right": lose_life,
    "straight": lose_mind
}

# ch = input("введите опцию: ")
# func_dict[ch]()


def summarizer(a, b, *args,  **kwargs):
    result = None
    if len(args) != 0:
        result = args[0]
        for el in args[1:]:
            result += el
    if result is not None:
        return a + b + result
    return a + b


# print(summarizer("sddsf", "dsfgdsf", "sdfsdf", "sdfsdf", "433434", t=1, g=3, k=4))


def func():

    def func_in_func():
        print(456)

    return func_in_func


print(func()())
