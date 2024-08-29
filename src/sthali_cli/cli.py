import typer

from .scripts.generate_docstring import main as main_docstring
from .scripts.generate_project import main as main_project
from .scripts.generate_requirements import main as main_requirements
from .scripts.generate_api_reference import main as main_api_reference

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
    main_project(project_name)


@app.command()
def generate_docstring():
    """Generate docstring based on pyproject.toml and docstrings from modules, classes and functions"""
    main_docstring()


@app.command()
def generate_requirements():
    """Generate ..."""
    main_requirements()


@app.command()
def generate_api_reference():
    """Generate ..."""
    main_api_reference()


@app.command()
def generate_docs():
    """Generate ..."""
    generate_requirements()
    generate_docstring()
    generate_api_reference()
