import datetime
import subprocess

import cookiecutter.main  # type: ignore
import typer


def main(project_name: str | None) -> None:
    if not project_name:
        pass
    typer.echo(f"Generating project with name: {project_name}")

    typer.echo("Cloning template")
    cookiecutter.main.cookiecutter(
        "https://github.com/jhunufernandes/sthali-core",
        no_input=True,
        overwrite_if_exists=True,
        extra_context={"project_name": project_name, "year": datetime.datetime.now().year},
    )

    typer.echo("Copying content")
    subprocess.call(["cp", "-r", f"./{project_name}/", "."])

    typer.echo("Deleting directory")
    subprocess.call(["rm", "-rf", f"./{project_name}"])
