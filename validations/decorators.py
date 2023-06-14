from functools import wraps

def get_atributes(func):
    @wraps(func)
    def wrapper(self, *arg, **kwargs):
        class_name = f"_{self.__class__.__name__}__"
        keys = list(self.__dict__.keys())
        values = list(self.__dict__.values())
        keys = map(lambda title: title.replace(class_name, ''), keys)
        data = dict(zip(keys, values))
        return func(self, data)
    return wrapper

def validate_seller(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        pass
    return wrapper