import mkdocs.commands.serve
import typer

from .scripts import Command, Generate

app = typer.Typer()
state = {}


@app.callback()
def callback() -> None:
    pass


@app.command()
def generate(command: Command, project_name: str | None = None) -> None:
    if command == Command.project and project_name is None:
        raise ValueError("Project name is required for project")

    generate_client = Generate(command, project_name)
    generate_client.execute()


@app.command()
def serve() -> None:
    config_file = "docs/mkdocs.yml"
    mkdocs.commands.serve.serve(config_file)
