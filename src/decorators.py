import datetime
from typing import Any, Callable, Optional, Union


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования переданных функций"""

    def my_decorator(func: Callable) -> Callable:
        def inner(*args: Any, **kwargs: Any) -> Any:

            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} OK\n"
            except Exception as error:
                result = None
                message = (
                    f"{func.__name__} Start_time = {start_time} "
                    f"End_time = {datetime.datetime.now()} error: {error}. Inputs: {args}, {kwargs}\n"
                )
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as log_file:
                        log_file.write(message)
                else:
                    print(message)

            return result

        return inner

    return my_decorator


@log("log.txt")
def _summ(a: Union[int, float], b: Union[int, float]) -> None:
    print(a + b)


# _summ(5, "12")
#  Start_time = {start_time} " f"End_time = {datetime.datetime.now()}\n
