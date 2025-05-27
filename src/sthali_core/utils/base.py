"""{...}."""

import typing

import fastapi
import pydantic


class Config:
    app_specification: dict[str, typing.Any]

    def __init__(self, app_specification_file_path: str) -> None:
        ...


@pydantic.dataclasses.dataclass
class AppSpecification:
    pass


class App:
    app: fastapi.FastAPI

    def __init__(self, app_specification: AppSpecification) -> None:
        ...

