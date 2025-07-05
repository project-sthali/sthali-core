"""Script to generate the requirements documentation from pyproject.toml.

This script reads the Python version, dependencies, and optional dependencies from pyproject.toml,
renders them into a Markdown template, and writes the result to the requirements documentation file.
"""

import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, TEMPLATES, File


def main(pyproject_content: dict[str, typing.Any]) -> None:
    """Generate the requirements documentation file.

    This function reads the Python version and dependencies from pyproject.toml,
    renders them into a Markdown template, and writes the output to the requirements file.
    """
    typer.echo("Generating requirements")

    typer.echo("Rendering the template with the data")
    requirements_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("requirements.md")  # type: ignore
    requirements_content: str = requirements_template.render(**pyproject_content)  # type: ignore

    typer.echo("Writing requirements")
    with File(DOCS_PATH / "requirements.md", "w") as requirements_file:
        requirements_file.write(requirements_content)

    typer.echo("Generated requirements")
