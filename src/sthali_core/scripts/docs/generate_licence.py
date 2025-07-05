"""Script to generate the license documentation file from the main LICENSE file.

This script write the content of the LICENSE file into it.
"""

import datetime
import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, ROOT_PATH, TEMPLATES, File


def main(pyproject_content: dict[str, typing.Any]) -> None:
    """Generate the license documentation file.

    This function write the content of the LICENSE file into the documentation file.
    """
    typer.echo("Generating license")

    typer.echo("Rendering the template with the data")
    license_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("license.md")  # type: ignore
    license_content: str = license_template.render(  # type: ignore
        **pyproject_content,
        year=datetime.datetime.now().year,
    )

    typer.echo("Writing licenses")
    with File(DOCS_PATH / "license.md", "w") as license_file:
        license_file.write(license_content)

    with File(ROOT_PATH / "LICENSE", "w") as license_file:
        license_file.write(license_content)

    typer.echo("Generated license")
