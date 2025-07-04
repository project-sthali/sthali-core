"""Script to generate the index file from pyproject.toml.

This script read contents from pyproject.toml, renders them into a Markdown template, and writes the result to the
index documentation file.
"""

import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, TEMPLATES, File


def main(pyproject_content: dict[str, typing.Any], organization_name: str) -> None:
    """Generate the index documentation file.

    This function read contents from pyproject.toml, renders them into a Markdown template, and writes the output to
    the index file.

    Args:
        pyproject_content (dict[str, typing.Any]): The content of pyproject.toml.
        organization_name (str): The name of the organization.
    """
    typer.echo("Generating index")

    typer.echo("Rendering the template with the data")
    index_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("index.md")  # type: ignore
    index_content: str = index_template.render(  # type: ignore
        **pyproject_content,
        organization_name=organization_name,
    )

    typer.echo("Writing index")
    with File(DOCS_PATH / "index.md", "w") as index_file:
        index_file.write(index_content)

    typer.echo("Generated index")
