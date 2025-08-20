# # """По мотивам https://habr.com/ru/companies/otus/articles/801595/"""
#
# class Descriptor:
#     def __get__(self, instance, owner):
#         if instance is not None:
#             value = instance.attr_2 * 1000
#         else:
#             value = 1000
#         return value
#
# class MyClass:
#     attr = Descriptor()
#
#     def __init__(self, attr_2):
#         self.attr_2 = attr_2
#
#
# my_object = MyClass(1)
# # print(my_object.attr)  # выведет 'значение'
# print(MyClass.attr)  # выведет 'значение'


# class Descriptor:
#     def __set__(self, instance, value):
#         print(f"Установка значения {value}")
#         self.value = value
#
#     def __get__(self, instance, owner):
#         print(id(self))
#         print("Логирование получения значения value")
#         return self.value
#
#     def __delete__(self, instance):
#         print("Удаление атрибута")
#         del self.value
#
# class MyClass:
#
#     attr = Descriptor()
#
#     def __init__(self, attr_2):
#         self.attr_2 = attr_2
#
# my_object = MyClass(100)
# # my_object.attr = 10  # выведет 'Установка значения 10'
# print(my_object.attr)
# del my_object.attr
# # c = 1


class Descriptor:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name, 'еще не установлено')

    def __set__(self, instance, value):
        setattr(instance, self.private_name, value)

class MyClass:
    attr = Descriptor()

my_object = MyClass()
print(my_object.attr)  # выведет 'еще не установлено'
my_object.attr = 99
print(my_object.attr)  # выведет 99

import time

class CachedAttribute:
    def __init__(self, method):
        self.method = method
        self.cache = {}

    def __get__(self, instance, owner):
        if instance not in self.cache:
            self.cache[instance] = self.method(self=instance)
        return self.cache[instance]


class HeavyComputation:
    @CachedAttribute
    def compute(self):
        # имитация длительного вычисления
        time.sleep(2)
        return "Результат вычисления"

hc = HeavyComputation()
start_time = time.time()
print(hc.compute)  # первый вызов занимает время
print(f"Выполнено за {time.time() - start_time} секунд")

start_time = time.time()
print(hc.compute)  # второй вызов мгновенный, использует кэшированный результат
print(f"Выполнено за {time.time() - start_time} секунд")