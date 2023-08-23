# telebot example
# from functools import wraps
#
# import telebot
# from telebot.types import Message
# from pprint import pprint
#
# bot = telebot.TeleBot("")
#
#
# @bot.message_handler(commands=["start", ])
# def efvsdfvsdfv(message: Message):
#     print("Hello")
#
#
# # bot.polling()
#
# def deco(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return inner
#
#
# class A:
#     def __init__(self, token):
#         self.token = token
#         self.command_mapper = {}
#
#     def add_new_commands_and_function(self, func, commands):
#         for command in commands:
#             self.command_mapper[command] = func
#
#     def message_handler(self, commands):
#         def outer(func):
#             self.add_new_commands_and_function(func=func, commands=commands)
#
#             @wraps(func)
#             def inner(*args, **kwargs):
#                 pprint(self.command_mapper)
#                 return func(*args, **kwargs)
#
#             return inner
#         return outer
#
#     def handle_command(self, command):
#         return self.command_mapper[command]()
#
#
# # def returner():
# #     return 123
#
#
# new_bot = A("sdfvsdfvsdfvdfsv")
# # print(a_object.message_handler())
#
#
# @new_bot.message_handler(commands=["start", "run", "menu"])
# def returner():
#     return 123
#
#
# @new_bot.message_handler(commands=["finish", ])
# def returner_2():
#     return 456
#
#
# # print(returner())
#
# print(new_bot.handle_command("run"))
# print(new_bot.handle_command("finish"))
#
#
# [
#     {"function": "func_1", "meta": "dfvsdfvd"},
#     {"function": "func_2", "meta": "dfvsdfvd"},
#     {"function": "func_3", "meta": "dfvsdfvd"},
#     {"function": "func_4", "meta": "dfvsdfvd"}
# ]









# flask example

from flask import Flask

app = Flask("test_app_name")


@app.route("/")
def hello():
    return "123"


app.run()
