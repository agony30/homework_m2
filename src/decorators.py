def log(filename=None):
    def decorator(func):
        def inner(*args, **kwargs):
            
            result = func(*args, **kwargs)
            return result
        return inner
    return decorator


# код проверки

@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(2, 3)
# my_function("g", 4)
