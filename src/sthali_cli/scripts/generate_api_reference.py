from os import getcwd, listdir
from os.path import join as path_join

from typer import echo

from .commons import read_file, write_file


def main():
    echo("Generating API Reference")
    root_path = getcwd()

    echo("Getting references")
    api_reference_dir = path_join(root_path, "docs/docs/api")
    api_references = sorted(listdir(api_reference_dir))

    echo("Reading mkdocs.yml")
    mkdocs_dir = path_join(root_path, "docs")
    mkdocs_path = path_join(mkdocs_dir, "mkdocs.yml")
    mkdocs_dict = read_file(mkdocs_path)

    echo("Rendering mkdocs_dict with the data")
    for section in mkdocs_dict["nav"]:
        if "API Reference" in section.keys():
            section["API Reference"] = [f"api/{i}" for i in api_references]

    echo("Writing mkdocs.yml")
    write_file(mkdocs_path, mkdocs_dict)
