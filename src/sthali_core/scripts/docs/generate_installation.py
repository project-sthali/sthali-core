"""Script to generate the installation file from pyproject.toml.

This script read contents from pyproject.toml, renders them into a Markdown template, and writes the result to the
installation documentation file.
"""

import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, TEMPLATES, File


def main(pyproject_content: dict[str, typing.Any], organization_name: str | None = None) -> None:
    """Generate the installation documentation file.

    This function read contents from pyproject.toml, renders them into a Markdown template, and writes the output to
    the installation file.

    Args:
        pyproject_content (dict[str, typing.Any]): The content of pyproject.toml.
        organization_name (str): The name of the organization.
    """
    typer.echo("Generating installation")

    typer.echo("Rendering the template with the data")
    installation_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("installation.md")  # type: ignore
    installation_content: str = installation_template.render(  # type: ignore
        **pyproject_content,
        organization_name=organization_name,
    )

    typer.echo("Writing installation")
    with File(DOCS_PATH / "installation.md", "w") as installation_file:
        installation_file.write(installation_content)

    typer.echo("Generated installation")
