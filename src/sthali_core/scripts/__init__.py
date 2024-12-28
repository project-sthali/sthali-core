"""The module that contains the CLI commands.

Classes:
    Command: The commands that can be executed by the CLI.
    Generate: The class that executes the commands based on the provided arguments.
"""
import enum

from .generate_api_reference import main as main_api_reference
from .generate_docstring import main as main_docstring
from .generate_licence import main as main_licence
from .generate_project import main as main_project
from .generate_readme import main as main_readme
from .generate_requirements import main as main_requirements


class Command(str, enum.Enum):
    """The commands that can be executed by the CLI.

    Options:
        api_reference
        docs
        docstring
        project
        readme
        requirements
    """
    api_reference = "api-reference"
    docs = "docs"
    docstring = "docstring"
    licence = "licence"
    project = "project"
    readme = "readme"
    requirements = "requirements"


class Generate:
    """The class that executes the commands based on the provided arguments.

    Attributes:
        command (Command): The command to be executed.
        project_name (str | None): The name of the project.

    Args:
        command (Command): The command to be executed.
        project_name (str | None): The name of the project.
            Defaults to None.

    Methods:
        execute: Executes the command based on the provided arguments.
    """
    def __init__(self, command: Command, project_name: str | None = None) -> None:
        """Initializes an instance of the class.

        Args:
            command (Command): The command to be executed.
            project_name (str | None): The name of the project.
                Defaults to None.
        """
        self.command = command
        self.project_name = project_name

    def execute(self) -> None:
        """Executes the command based on the provided arguments."""
        command = self.command
        match command:
            case Command.api_reference:
                main_api_reference()

            case Command.docs:
                main_requirements()
                main_readme()

                main_docstring()
                main_api_reference()

                main_licence()

            case Command.docstring:
                main_docstring()

            case Command.licence:
                main_licence()

            case Command.project:
                main_project(self.project_name)
                main_licence()

            case Command.readme:
                main_readme()

            case Command.requirements:
                main_requirements()
