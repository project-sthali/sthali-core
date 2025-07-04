"""Common utility functions and classes used across the CLI scripts.

Variables:
    ROOT_PATH (pathlib.Path): The root path of the project.
    README_FILE_PATH (pathlib.Path): The path to the README.md file.
    BASE_DOCS_PATH (pathlib.Path): The base path to the docs directory.
    DOCS_PATH (pathlib.Path): The path to the docs directory.
    API_REFERENCE_PATH (pathlib.Path): The path to the api directory.

    PROJECT_NAME (str): The name of the project.
    PROJECT_SLUG (str): The slug of the project.

    TEMPLATES (fastapi.templating.Jinja2Templates): The Jinja2 templates for rendering.

Functions:
    to_snake_case(string: str) -> str: Converts a given string to snake case.
    read_pyproject() -> dict[str, typing.Any]: Reads the pyproject.toml file and returns its content as a dictionary.

Classes:
    File: A context manager class to handle file operations.
"""

import pathlib
import re
import typing

import fastapi.templating
import tomli


def to_snake_case(string: str) -> str:
    """Converts a given string to snake case.

    Args:
        string (str): The string to be converted.

    Returns:
        str: The converted string in snake case.
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return re.sub(r"-", "_", s2).lower()


def read_pyproject() -> dict[str, typing.Any]:
    """Reads the pyproject.toml file and returns its content as a dictionary.

    Returns:
        dict[str, typing.Any]: The content of the pyproject.toml file as a dictionary
    """
    with File(ROOT_PATH / "pyproject.toml") as pyproject_file:
        return tomli.loads(pyproject_file.read())


# paths
ROOT_PATH = pathlib.Path.cwd()
README_FILE_PATH = ROOT_PATH / "README.md"
BASE_DOCS_PATH = ROOT_PATH / "docs"
DOCS_PATH = BASE_DOCS_PATH / "docs"
API_REFERENCE_PATH = DOCS_PATH / "api"

# project metadata
PROJECT_NAME = ROOT_PATH.name.split("/")[-1]
PROJECT_SLUG = to_snake_case(PROJECT_NAME)

# templates
TEMPLATES = fastapi.templating.Jinja2Templates(ROOT_PATH / "src" / "sthali_core" / "scripts" / "templates")

class File:
    """A context manager class to handle file operations.

    Args:
        file_path (Path): The path to the file.
        mode (typing.Literal["r", "w"], optional): The mode in which the file should be opened.
            Defaults to "r".

    Methods:
        reset: Resets the file at the specified file path.
    """

    def __init__(self, file_path: pathlib.Path, mode: typing.Literal["r", "w"] = "r") -> None:
        """Initializes an instance of the class.

        Args:
            file_path (Path): The path to the file.
            mode (typing.Literal["r", "w"], optional): The mode in which the file should be opened.
                Defaults to "r".
        """
        self.file_path = file_path
        self.mode = mode

    def __enter__(self) -> typing.IO[typing.Any]:
        """Context manager method that is called when entering a `with` statement.

        Returns:
            file object (typing.IO[typing.Any]): The opened file object.
        """
        return pathlib.Path(self.file_path).open(self.mode)

    def __exit__(self, *args: object, **kwargs: typing.Any) -> None:
        """Exit the context manager.

        Args:
            args (object): The positional arguments passed to the __exit__ method.
            kwargs (typing.Any): The keyword arguments passed to the __exit__ method.
        """

    def reset(self) -> None:
        """Resets the file at the specified file path."""
        with pathlib.Path(self.file_path).open():
            pass
