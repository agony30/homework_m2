from typing import Union, Any

from src.decorators import log


def test_log_output(capsys: Any) -> None:

    @log()
    def add_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a + b

    add_numbers(5, 6)
    captured = capsys.readouterr()
    assert captured.out == "add_numbers OK\n\n"


def test_log_in_file() -> None:

    file_name = "log.txt"

    @log(file_name)
    def sub_numbers(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        return a - b

    sub_numbers(8, 4)
    with open(file_name, "r", encoding="utf-8") as log_file:
        assert log_file.readlines()[-1] == "sub_numbers OK\n"
