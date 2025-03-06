def log(filename=None):
    def my_decorator(func):
        def inner(*args, **kwargs):

            try:
                result = func(*args, **kwargs)
                message = f'{func.__name__} OK\n'
            except Exception as error:
                result = None
                message = f'{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n'
            finally:
                if filename:
                    with open(filename, "a", encoding='utf-8') as log_file:
                        log_file.write(message)
                else:
                    print(message)

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


@log("log.txt")
def summ(a, b):
    print(a+b)

summ("5", 12)
