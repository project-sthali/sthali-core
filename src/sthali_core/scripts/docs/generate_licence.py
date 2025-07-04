"""Script to generate the license documentation file from the main LICENSE file.

This script write the content of the LICENSE file into it.
"""

import typer

from ..commons import DOCS_PATH, ROOT_PATH, File


def main() -> None:
    """Generate the license documentation file.

    This function write the content of the LICENSE file into the documentation file.
    """
    typer.echo("Generating license")

    with File(DOCS_PATH / "license.md", "w") as license_doc_file, File(ROOT_PATH / "LICENSE") as license_file:
        license_file_content = license_file.read()
        license_doc_file.write(license_file_content)

    typer.echo("Generated license")
