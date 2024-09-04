from pathlib import Path
from re import sub
from typing import Literal, Any


def to_snake_case(string: str) -> str:
    s1 = sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    s2 = sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return sub(r"-", "_", s2).lower()


# paths
ROOT_PATH = Path.cwd()

PYPROJECT_FILE_PATH = ROOT_PATH / "pyproject.toml"

README_FILE_PATH = ROOT_PATH / "README.md"

MKDOCS_FILE_PATH = ROOT_PATH / "docs" / "mkdocs.yml"

DOCS_PATH = ROOT_PATH / "docs" / "docs"

REQUIREMENTS_PATH = ROOT_PATH / "docs" / "docs" / "requirements.md"

API_REFERENCE_PATH = ROOT_PATH / "docs" / "docs" / "api"


# files


# project metadata
PROJECT_NAME = ROOT_PATH.name.split("/")[-1]
PROJECT_SLUG = to_snake_case(PROJECT_NAME)


class File:
    def __init__(self, file_path: Path, mode: Literal["r", "w"] = "r") -> None:
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        #
        return Path(self.file_path).open(self.mode)

    def __exit__(self, *args: Any, **kwargs: Any):
        pass

    def reset(self):
        with Path(self.file_path).open():
            pass
