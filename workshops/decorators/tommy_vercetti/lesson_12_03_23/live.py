# data_dict = {
#     "data": {
#         "items":
#             {
#                 "users":
#                     [
#                         {
#                             "id": 123
#                         },
#                         {
#                             "id": 456
#                         }
#                     ]
#             }
#     }
# }
#
#
# # todo дз
# def get_in():
#     pass
#
#
# get_in("data", "items", "users", 0, "id", data_dict)
#
# # todo usage None

# с = 1
# print("программа началась")


# def black_box():
#     pass


# print(black_box)
# data_about_variable = id(black_box)
# print(data_about_variable)
# result = black_box()


# variable = black_box
# black_box = 1
# print(variable)
# print(black_box)
# print(variable)
# black_box = variable
# print(black_box)

# print = 1
# print(print)
# print(sum)

# print("программа закончилась")
# sum = 100
# sum([1, 2, 3, 4])


# result = black_box()
# print(result)
# print(variable)
# print(variable())


def black_box(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 + num_2
    elif operation == "/":
        return num_1 + num_2
    else:
        print("Операция некорректна!")


# num_1 = 1
# num_2 = 2
# operation = "+"
# print(black_box)
# print(black_box(num_1, operation, num_2))

print(print)
print(print(4563456))
