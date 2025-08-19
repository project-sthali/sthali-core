"""Common utility functions and classes used across the CLI scripts.

Variables:
    ROOT_PATH (pathlib.Path): The root path of the project.
    DOCS_PATH (pathlib.Path): The path to the docs directory.
    TEMPLATES_PATH (pathlib.Path): The path to the templates directory.
    TEMPLATES (fastapi.templating.Jinja2Templates): Jinja2 templates for rendering documentation.

Functions:
    to_snake_case(string: str) -> str: Converts a given string to snake case.
    read_pyproject(path: pathlib.Path | None) -> dict[str, typing.Any]: Reads the pyproject.toml file and returns its
        content as a dictionary.
"""

import pathlib
import re
import typing

import fastapi.templating
import tomli

ROOT_PATH = pathlib.Path()
DOCS_PATH = ROOT_PATH / "docs" / "docs"
TEMPLATES_PATH = pathlib.Path(__file__).parent / "templates"
TEMPLATES = fastapi.templating.Jinja2Templates(TEMPLATES_PATH)


def read_pyproject(path: pathlib.Path | None = None) -> dict[str, typing.Any]:
    """Reads the pyproject.toml file and returns its content as a dictionary.

    Args:
        path (pathlib.Path): The path to the pyproject.toml file. Defaults to None.

    Returns:
        dict[str, typing.Any]: The content of the pyproject.toml file as a dictionary
    """
    path = ROOT_PATH / "pyproject.toml" or path
    with pathlib.Path.open(path) as pyproject_file:
        return tomli.loads(pyproject_file.read())


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
