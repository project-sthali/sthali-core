from subprocess import call
from cookiecutter.main import cookiecutter


# cookiecutter("https://github.com/jhunufernandes/sthali-project-template")
cookiecutter("https://github.com/jhunufernandes/sthali-cli")

project_name = "sthali-batatassauro"


def move_content():
    call(["mv", f"./{project_name}/*", f"./{project_name}/.*", "."])


def delete_directory():
    call(["rm", "-rf", "./{project_name}"])
