from typer import echo

from subprocess import call
from cookiecutter.main import cookiecutter  # type: ignore


def main(project_name: str) -> None:
    echo(f"Generating project with name: {project_name}")

    echo("Cloning template")
    cookiecutter(
        "https://github.com/jhunufernandes/sthali-cli",
        no_input=True,
        overwrite_if_exists=True,
        extra_context={"project_name": project_name},
    )

    echo("Copying content")
    call(["cp", "-r", f"./{project_name}/", "."])

    echo("Deleting directory")
    call(["rm", "-rf", f"./{project_name}"])

    echo("Copying LICENCE")
    call(["cp", "./LICENSE", "./docs/docs/license.md"])
