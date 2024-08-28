import typer
from .scripts.generate_project import generate as generate_prjct
from .scripts.generate_docs import generate as generate_dcs

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
    """Generate a docs based on docstring"""
    generate_dcs()
