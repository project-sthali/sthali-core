from os import listdir

from typer import echo
from yaml import dump, safe_load

from .commons import API_REFERENCE_PATH, MKDOCS_FILE_PATH, File


def main():
    echo("Generating API Reference")

    echo("Getting references")
    api_references = sorted(listdir(API_REFERENCE_PATH))

    echo("Reading mkdocs.yml")
    with File(MKDOCS_FILE_PATH) as mkdocs_file:
        mkdocs_dict = safe_load(mkdocs_file.read())

    echo("Rendering mkdocs_dict with the data")
    for section in mkdocs_dict["nav"]:
        if "API Reference" in section.keys():
            section["API Reference"] = [{i.strip(".md"): f"api/{i}"} for i in api_references]

    echo("Writing mkdocs.yml")
    with File(MKDOCS_FILE_PATH) as mkdocs_file:
        dump(mkdocs_dict, mkdocs_file)
