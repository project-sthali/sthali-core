import typer

from .scripts import Command, Generate

app = typer.Typer()
state = {}


@app.callback()
def callback():
    pass


@app.command()
def generate(command: Command, project_name: str | None = None):
    if command == Command.project and project_name is None:
        raise ValueError("Project name is required for project")

    generate_client = Generate(command, project_name)
    generate_client.execute()
