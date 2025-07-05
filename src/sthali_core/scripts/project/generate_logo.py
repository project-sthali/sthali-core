"""{...}."""
import typing

import typer

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import DOCS_PATH, TEMPLATES, File


def main(project_name: str) -> None:
    """{...}."""
    typer.echo("Generating logo")

    typer.echo("Rendering the template with the data")
    logo_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("logo.svg")  # type: ignore
    logo: str = logo_template.render(project_name=project_name)  # type: ignore

    typer.echo("Writing logo")
    with File(DOCS_PATH / "images" / f"{project_name}.svg", "w") as logo_file:
        logo_file.write(logo)

    typer.echo("Generated logo")
