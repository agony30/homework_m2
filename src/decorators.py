def log(filename=25):
    def my_decorator(func):
        def inner(*args, **qwargs):
            print(f"Аргументы декоратора: {filename}")
            result = func(*args, **qwargs)
            return result
        return inner
    return my_decorator

# def log(arg1=7):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             print(f"Аргументы декоратора: {arg1}")
#             result = func(*args, **kwargs)
#             print("После выполнения функции")
#             return result
#         return wrapper
#     return my_decorator


@log()
def summ(a, b):
    print(a+b)

summ(1, 30)
