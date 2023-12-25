import os
import pathlib
from typing import Tuple, List, Union
import requests


def get_latest_ver() -> str:
    req = requests.get("https://pypi.org/pypi/denilson-fib-py/json")
    return req.json()["info"]["version"]


def unpack_ver(ver: str) -> Tuple[int, int, int]:
    verb: List[str] = ver.split(".")
    return int(verb[0]), int(verb[1]), int(verb[2])


def increase_ver(verb: Union[Tuple[int, int, int], List[int]]) -> List[int]:
    first: int = verb[0]
    second: int = verb[1]
    third: int = verb[2]

    third += 1
    if third >= 10:
        third = 0
        second += 1
        if second >= 10:
            second = 0
            first += 1
    return [first, second, third]


def pack_ver(verb: Union[Tuple[int, int, int], List[int]]) -> str:
    return f"{verb[0]}.{verb[1]}.{verb[2]}"


def write_ver_to_file(ver: str) -> None:
    ver_file_path = str(pathlib.Path(
        __file__).parent.absolute()) + "/fib_py/version.py"
    if os.path.exists(ver_file_path):
        os.remove(ver_file_path)
    with open(ver_file_path, "w") as f:
        f.write(f"VERSION='{ver}'")


if __name__ == "__main__":
    write_ver_to_file(ver=pack_ver(verb=increase_ver(
        verb=unpack_ver(ver=get_latest_ver()))))
