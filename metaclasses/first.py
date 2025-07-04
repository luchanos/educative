new_class = type("MyClass", (object,), {"a": 1, "b": 2, "method": lambda x: x})
new_obj = new_class()
# print(new_obj)

print(isinstance(type, type)) # логично
print(isinstance(type, object)) #
print(isinstance(object, type))

class MyBaseClass:
    pass

class MyClass:
    pass

c = MyClass()
print(isinstance(c, MyClass))
print(isinstance(c, MyBaseClass))

print(type(type(type)))
print(type(object))
