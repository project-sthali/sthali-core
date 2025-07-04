"""Script to generate the index file from pyproject.toml.

This script read contents from pyproject.toml, renders them into a Markdown template, and writes the result to the
index documentation file.
"""

"""Script to generate and update the API Reference section in mkdocs.yml based on available API reference files."""
import pathlib
import typing

import typer
import yaml

if typing.TYPE_CHECKING:
    import fastapi.templating

from ..commons import API_REFERENCE_PATH, BASE_DOCS_PATH, TEMPLATES, File


def main(pyproject_content: dict[str, typing.Any], organization_name: str | None = None) -> None:
    """Generate and update the API Reference section in mkdocs.yml.

    This function scans the API reference directory, updates the 'API Reference' section
    in the mkdocs.yml navigation, and writes the changes back to the file.
    """
    typer.echo("Generating API Reference")

    typer.echo("Rendering the template with the data")
    mkdocs_template: fastapi.templating.Jinja2Templates = TEMPLATES.get_template("mkdocs.yml")  # type: ignore
    mkdocs_content: str = mkdocs_template.render(  # type: ignore
        **pyproject_content,
        organization_name=organization_name,
    )

    typer.echo("Writing temp mkdocs")
    with File(BASE_DOCS_PATH / "mkdocs.yml", "w") as mkdocs_file:
        mkdocs_file.write(mkdocs_content)

    typer.echo("Reading temp mkdocs")
    with File(BASE_DOCS_PATH / "mkdocs.yml") as mkdocs_file:
        mkdocs_dict = yaml.safe_load(mkdocs_file.read())

    typer.echo("Getting references")
    api_references = sorted([i.name for i in pathlib.Path.iterdir(API_REFERENCE_PATH)])

    typer.echo("Rendering mkdocs_dict with the data")
    for section in mkdocs_dict["nav"]:
        if "API Reference" in section:
            section["API Reference"] = [
                {"_".join(i.split("_")[1:]).rsplit(".", 1)[0]: f"api/{i}"} for i in api_references
            ]

    typer.echo("Writing mkdocs")
    with File(BASE_DOCS_PATH / "mkdocs.yml", "w") as mkdocs_file:
        yaml.dump(mkdocs_dict, mkdocs_file)

    typer.echo("Generated API Reference")
