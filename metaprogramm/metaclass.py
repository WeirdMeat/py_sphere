class CustomMeta(type):
    def __init__(cls, name, bases, dct):
        for i in dct:
            if i != '__module__' and i != '__qualname__':
                super().__setattr__("custom_" + i, super().__getattribute__(i))
                super().__delattr__(i)
