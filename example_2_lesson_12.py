class MyClass:
    def __new__(cls, *args, **kwargs):
        print("__new__")
        instance = object.__new__(cls)
        return instance

    def __init__(self, value):
        print("__init__")
        self.value = value

    def __del__(self):
        print("__del__")


my_class = MyClass(15)
print(15)