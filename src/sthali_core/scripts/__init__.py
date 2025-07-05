"""The module that contains the CLI commands.

Classes:
    Command: The commands that can be executed by the CLI.
    Generate: The class that executes the commands based on the provided arguments.
"""

import enum

from .commons import read_pyproject
from .docs.generate_docstring import main as main_docstring
from .docs.generate_index_file import main as main_index
from .docs.generate_installation import main as main_installation
from .docs.generate_licence import main as main_licence
from .docs.generate_mkdocs import main as main_mkdocs
from .docs.generate_readme import main as main_readme
from .docs.generate_requirements import main as main_requirements
from .docs.generate_usage import main as main_usage
from .project.generate_logo import main as main_logo
from .project.generate_project import main as main_project
from .project.update_pyproject_dependencies import main as update_pyproject_dependencies


class Generate:
    """The class that executes the options based on the provided arguments.

    Methods:
        execute: Executes the option based on the provided arguments.
    """

    class GenerateOptionsEnum(str, enum.Enum):
        """The options that can be executed by the CLI.

        Options:
            docs
            docstring
            index-file
            installation
            licence
            logo
            mkdocs
            project
            readme
            requirements
            usage
        """

        docs = "docs"
        docstring = "docstring"
        index_file = "index-file"
        installation = "installation"
        licence = "licence"
        logo = "logo"
        mkdocs = "mkdocs"
        project = "project"
        readme = "readme"
        requirements = "requirements"
        usage = "usage"

    @staticmethod
    def execute(option: GenerateOptionsEnum, project_name: str | None = None) -> None:
        """Executes the option based on the provided arguments."""
        pyproject_content = read_pyproject()
        organization_name = "project-sthali"
        match option:
            case Generate.GenerateOptionsEnum.docs:
                main_index(pyproject_content, organization_name)
                main_requirements(pyproject_content)
                main_installation(pyproject_content, organization_name)
                main_usage()
                main_readme()

                main_docstring()
                main_mkdocs(pyproject_content, organization_name)

                main_licence(pyproject_content)

            case Generate.GenerateOptionsEnum.docstring:
                main_docstring()

            case Generate.GenerateOptionsEnum.index_file:
                main_index(pyproject_content, organization_name)

            case Generate.GenerateOptionsEnum.installation:
                main_installation(pyproject_content, organization_name)

            case Generate.GenerateOptionsEnum.licence:
                main_licence(pyproject_content)

            case Generate.GenerateOptionsEnum.logo:
                assert project_name is not None, "Project name is required for project"
                main_logo(project_name)

            case Generate.GenerateOptionsEnum.mkdocs:
                main_mkdocs(pyproject_content, organization_name)

            case Generate.GenerateOptionsEnum.project:
                assert project_name is not None, "Project name is required for project"
                main_project(project_name)
                main_logo(project_name)
                main_licence(pyproject_content)

            case Generate.GenerateOptionsEnum.readme:
                main_readme()

            case Generate.GenerateOptionsEnum.requirements:
                main_requirements(pyproject_content)

            case Generate.GenerateOptionsEnum.usage:
                main_usage()


class Update:
    """The class that executes the options based on the provided arguments.

    Methods:
        execute: Executes the option based on the provided arguments.
    """

    class UpdateOptionsEnum(str, enum.Enum):
        """The options that can be executed by the CLI."""

        requirements = "requirements"

    @staticmethod
    def execute(option: UpdateOptionsEnum) -> None:
        """Executes the option based on the provided arguments."""
        match option:
            case Update.UpdateOptionsEnum.requirements:
                update_pyproject_dependencies()
