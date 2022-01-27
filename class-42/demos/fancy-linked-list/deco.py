from functools import wraps
from time import sleep


def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_val_from_original_function = func(*args, **kwargs)
        emphasized = return_val_from_original_function.upper() + "!!!"
        return emphasized

    return wrapper


@emphasize
def say(txt):
    return txt


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


@procrastinate
def loop():
    for i in range(10):
        print(i)


print(say("hola bambina"))
loop()
