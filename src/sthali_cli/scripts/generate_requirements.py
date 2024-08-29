from importlib import import_module
from os import getcwd, makedirs
from os.path import join as path_join
from re import sub

from typer import echo


def generate():
    echo("Generating requirements")

    with open("pyproject.toml", "rb") as f:
        echo("Reading pyproject.toml")
        toml_dict = tomli.load(f)

    echo("Getting dependencies")
    dependencies = toml_dict['project']['dependencies']
    optional_dependencies = toml_dict['project']['optional-dependencies']

    requirements = ""

    # {'dev': ['coverage[toml] >= 7.6.1', 'ruff >= 0.5.2'], 'tests': ['coverage[toml] >= 7.6.1'], 'stage': ['build >= 1.2.1', 'coverage[toml] >= 7.6.1']}

    root_path = getcwd()
    requirements_dir = path_join(root_path, "docs/docs/api")
    filename = "requirements.md"
    filepath = path_join(requirements_dir, filename)

    # Ensure the directory exists
    makedirs(requirements_dir, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        echo("Writing requirements")
        f.write(requirements)



def to_snake_case(string: str) -> str:
    s1 = sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    s2 = sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return sub(r"-", "_", s2).lower()
