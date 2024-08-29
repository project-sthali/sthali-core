from typing import Any
from re import sub

import yaml
from tomli import load


def to_snake_case(string: str) -> str:
    s1 = sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    s2 = sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return sub(r"-", "_", s2).lower()


def read_file(file_path: str) -> Any:
    with open(file_path, "rb") as file:
        file_extension = file_path.split(".")[-1]
        if file_extension == "toml":
            return load(file)
        elif file_extension == "yml":
            return yaml.safe_load(file)


def write_file(file_path: str, data: str | dict[str, Any]) -> None:
    with open(file_path, "w") as file:
        file_extension = file_path.split(".")[-1]
        if file_extension == "yml":
            yaml.dump(data, file, default_flow_style=False)
        elif file_extension == "md":
            file.write(str(data))
