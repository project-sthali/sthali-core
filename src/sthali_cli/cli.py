import typer

from .scripts.generate_docstring import generate as generate_dcstrng
from .scripts.generate_project import generate as generate_prjct

app = typer.Typer()


@app.callback()
def callback():
    typer.echo("callback")


@app.command()
def generate_project(project_name: str):
    """Generate a new project based on coockiecutter template

    Attributes:
        project_name (str): Name of the project
    """
    generate_prjct(project_name)


@app.command()
def generate_docs():
    """Generate docs based on pyproject.toml and docstrings from modules, classes and functions"""
    generate_dcstrng()
