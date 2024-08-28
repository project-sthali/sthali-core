import typer
from .scripts.generate_project import generate_project

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
    generate_project(project_name)


@app.command()
def generate_docs():
    """Generate a docs based on docstring"""
    typer.echo("generate_docs")
