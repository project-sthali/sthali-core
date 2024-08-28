from typer import echo

from subprocess import call
from cookiecutter.main import cookiecutter


def generate_project(project_name: str) -> None:
    echo(f"Generating project with name: {project_name}")
    clone_template()
    move_content(project_name)
    delete_directory(project_name)


def clone_template() -> None:
    echo("Cloning template")
    cookiecutter("https://github.com/jhunufernandes/sthali-cli", no_input=True, overwrite_if_exists=True)


def move_content(project_name: str) -> None:
    echo("Moving content")
    call(["mv", f"./{project_name}/*", f"./{project_name}/.*", "."])


def delete_directory(project_name: str) -> None:
    echo("Deleting directory")
    call(["rmdir", f"./{project_name}"])
