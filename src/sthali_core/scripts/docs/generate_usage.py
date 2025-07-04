"""Script to generate the usage file from pyproject.toml.

This script read contents from pyproject.toml, renders them into a Markdown template, and writes the result to the
usage documentation file.
"""
import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, TEMPLATES, File


def main() -> None:
    """Generate the usage documentation file.

    This function read contents from pyproject.toml, renders them into a Markdown template, and writes the output to
    the usage file.
    """
    typer.echo("Generating usage")

    typer.echo("Rendering the template with the data")
    usage_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("usage.md")  # type: ignore
    usage: str = usage_template.render()  # type: ignore

    typer.echo("Writing usage")
    with File(DOCS_PATH / "usage.md", "w") as usage_file:
        usage_file.write(usage)

    typer.echo("Generated usage")
