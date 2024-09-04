from typer import echo

from .commons import DOCS_PATH, README_FILE_PATH, File

files_used_in_readme = ["index", "requirements", "installation", "usage"]


def main():
    echo("Generating readme")

    echo("Clearing readme")
    with File(README_FILE_PATH, "w") as readme_file:
        readme_file.write("\n")

    with readme_file as readme_file:
        docs_files_path_with_extension = [DOCS_PATH / f"{i}.md" for i in files_used_in_readme]
        for doc_file_path in docs_files_path_with_extension:
            echo(f"Concatenating doc: {doc_file_path.name}")
            with File(doc_file_path) as doc_file:
                doc_file_content = doc_file.read()
                readme_file.write(doc_file_content)
