# class LoggedAttribute:
#     def __init__(self):
#         self.overrided = False
#
#     def __set_name__(self, owner, name):
#         self.private_name = '_' + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.private_name, None)
#
#     def __set__(self, instance, value, *args, **kwargs):
#         if self.overrided:
#             print(f"Попытка переопределить {self.private_name} в {value}")
#             raise Exception('Unable to override!')
#         self.overrided = True
#         print(f"Установка {self.private_name} в {value}")
#         setattr(instance, self.private_name, value)
#
# class User:
#     name: str = LoggedAttribute()
#     age: int = LoggedAttribute()
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# u = User("Katya", 30)
# u.name = "Katyuha"  # Логируется изменение
# u.age = 31  # Логируется изменение


class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __get__(self, instance, owner):
        if self.instance is None:
            self.instance = self.cls()
        return self.instance

class Database:
    def __init__(self):
        print("Создание базы данных")

# применение дескриптора Singleton
class AppConfig:
    db = Singleton(Database)

# тестирование паттерна Singleton
config1 = AppConfig()
config2 = AppConfig()
db1 = config1.db  # создание БД
db2 = config2.db  # не создает новый экземпляр, использует существующий

print(db1 is db2)  # выведет True, подтверждая, что db1 и db2 - один и тот же объект
