from os import getcwd
from os.path import join as path_join
from subprocess import call

from typer import echo


def main():
    echo("Generating readme")
    root_path = getcwd()

    echo("Concatenating docs")
    docs_dir = path_join(root_path, "docs/docs")
    x1 = " ".join([path_join(docs_dir, f"{i}.md") for i in ["index", "requirements", "installation", "usage"]])
    x2 = path_join(root_path, 'README.md')
    call(f"cat {x1} > {x2}", shell=True)
