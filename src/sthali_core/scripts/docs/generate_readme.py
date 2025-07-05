"""Script to generate the README file by concatenating selected documentation files.

This script append the contents of specified documentation files in order.
"""

import typer

from ..commons import DOCS_PATH, README_FILE_PATH, File

FILES_USED_IN_README = ["index", "requirements", "installation", "usage"]


def main() -> None:
    """Generate the README file by concatenating documentation files.

    This function write the content of 'index.md', 'requirements.md', 'installation.md', and 'usage.md' from the docs
    directory into the README file.
    """
    typer.echo("Generating readme")

    with File(README_FILE_PATH, "w") as readme_file:
        docs_files_path_with_extension = [DOCS_PATH / f"{i}.md" for i in FILES_USED_IN_README]
        for doc_file_path in docs_files_path_with_extension:
            typer.echo(f"Concatenating doc: {doc_file_path.name}")
            with File(doc_file_path) as doc_file:
                doc_file_content = doc_file.read()
                readme_file.write(doc_file_content)
                readme_file.write("\n")

    typer.echo("Generated readme")
