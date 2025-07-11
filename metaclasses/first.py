class MyClass:
    a = 1
    b = 2

    def method(self, x):
        return x


#
# print(MyClass)
# print(type(MyClass))

# some_data = [("Test1", {"m": 1, "n": 2, "func": lambda x, y: x + y}),
#              ("Test2", {"c": 3, "d": 4}),
#              ("Test3", {"i": 5, "j": 6, "x": 123})]
#
# for item in some_data:
#     new_class = type(item[0], (object,), item[1])
#     print(new_class)
#     print(new_class.__dict__)

# new_class = type("MyClass", (object,), {"a": 1, "b": 2, "method": lambda x: x})
# new_obj = new_class()
# print(new_obj)

# print(isinstance(type, type)) # логично
# print(isinstance(type, object)) #
# print(isinstance(object, type))
#
# class MyBaseClass:
#     pass
#
# class MyClass:
#     pass
#
# c = MyClass()
# print(isinstance(c, MyClass))
# print(isinstance(c, MyBaseClass))

# print(type(type(type)))
# print(type(object))

# A simple metaclass that just prints what it's creating
class MyMeta(type):
    def __new__(mcs, name, bases, dct):
        print("---------------------------------")
        print(f"Creating class: {name}")
        print(f"Parent classes: {bases}")
        print(f"Attributes/methods: {dct}")

        # We must call the parent's __new__ to actually create the class
        new_class = super().__new__(mcs, name, bases, dct)
        print("---------------------------------")
        return new_class


# Now, let's use our metaclass
class MyClass(metaclass=MyMeta):
    x = 50

    def greet(self):
        print("Hello there!")


print("\n...Python script continues...")
my_instance = MyClass()  # This line runs AFTER the metaclass has done its job


class EnforceDocs(type):
    def __new__(mcs, name, bases, dct):
        # Check every item in the class dictionary
        for key, value in dct.items():
            # If it's a function...
            if callable(value):
                # ...and it doesn't have a docstring...
                if not getattr(value, '__doc__'):
                    # ...raise an error!
                    raise TypeError(f"Method '{key}' in class '{name}' must have a docstring.")

        # If all checks pass, create the class as normal
        return super().__new__(mcs, name, bases, dct)


# --- Let's try to use it ---

# This will work
class WellBehavedClass(metaclass=EnforceDocs):
    def my_method(self):
        """This is a good method with a docstring."""
        pass


# This will FAIL when Python tries to define it
try:
    class BadlyBehavedClass(metaclass=EnforceDocs):
        def another_method(self):
            # No docstring here!
            pass
except TypeError as e:
    print(f"Caught expected error: {e}")

# A simple registry to hold our plugins
PLUGIN_REGISTRY = {}


class PluginMeta(type):
    def __new__(mcs, name, bases, dct):
        # Create the class first
        new_class = super().__new__(mcs, name, bases, dct)

        # If the class has a 'plugin_name' attribute, register it
        if 'plugin_name' in dct:
            plugin_name = dct['plugin_name']
            PLUGIN_REGISTRY[plugin_name] = new_class
            print(f"Registered plugin: '{plugin_name}'")

        return new_class


# A base class for all our plugins
class PluginBase(metaclass=PluginMeta):
    pass


# Now, developers can just create plugins by inheriting from PluginBase
class ImageProcessor(PluginBase):
    plugin_name = "image_processor"

    def process(self, image):
        print("Processing image...")


class SoundProcessor(PluginBase):
    plugin_name = "sound_processor"

    def process(self, sound):
        print("Processing sound...")


class UnregisteredPlugin(PluginBase):
    # This one won't be registered because it's missing 'plugin_name'
    pass


print("\nAvailable plugins:")
print(PLUGIN_REGISTRY)
