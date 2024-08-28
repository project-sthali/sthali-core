from importlib import import_module
from os.path import abspath, dirname
from os.path import join as path_join
from re import sub

from typer import echo


def generate():
    echo("Generating docs")

    echo("Getting project name")
    project_name = dirname(__file__).split("/")[-3]
    project_slug = to_snake_case(project_name)

    echo("Getting project module")
    project_module = import_module(project_slug)

    echo("Getting imports from module")
    imports = project_module.__all__

    for i in imports:
        attr = getattr(project_module, i)
        doc = attr.__doc__
        filename = f"_{to_snake_case(i)}.md"
        filepath = path_join(abspath(dirname(__file__)), "../docs", filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(doc)


def to_snake_case(string: str) -> str:
    s1 = sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    s2 = sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return sub(r"-", "_", s2).lower()
