"""The module that contains the CLI commands.

Classes:
    Command: The commands that can be executed by the CLI.
    Generate: The class that executes the commands based on the provided arguments.
"""

import enum

from .commons import DOCS_PATH, ROOT_PATH, read_pyproject
from .docs import BaseDocsGenerator
from .docs.generate_docstring import main as main_docstring
from .docs.generate_mkdocs import main as main_mkdocs
from .project.generate_project import main as main_project


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
        docs_generator = BaseDocsGenerator(pyproject_content, organization_name, project_name)

        match option:
            case Generate.GenerateOptionsEnum.docs:
                Generate.execute(Generate.GenerateOptionsEnum.licence)

                Generate.execute(Generate.GenerateOptionsEnum.index_file)
                Generate.execute(Generate.GenerateOptionsEnum.requirements)
                Generate.execute(Generate.GenerateOptionsEnum.installation)
                Generate.execute(Generate.GenerateOptionsEnum.usage)
                Generate.execute(Generate.GenerateOptionsEnum.readme)

                Generate.execute(Generate.GenerateOptionsEnum.docstring)
                Generate.execute(Generate.GenerateOptionsEnum.mkdocs)

            case Generate.GenerateOptionsEnum.docstring:
                main_docstring()

            case Generate.GenerateOptionsEnum.index_file:
                docs_generator.render("index.md")

            case Generate.GenerateOptionsEnum.installation:
                docs_generator.render("installation.md")

            case Generate.GenerateOptionsEnum.licence:
                docs_generator.render("license.md")
                path = ROOT_PATH
                docs_generator.render("license.md", path=path, new_file="LICENSE")

            case Generate.GenerateOptionsEnum.logo:
                assert project_name is not None, "Project name is required for project"
                path = DOCS_PATH / "images"
                docs_generator.render("logo.svg", path=path)

            case Generate.GenerateOptionsEnum.mkdocs:
                Generate.execute(Generate.GenerateOptionsEnum.docstring)

                # prerender mkdocs.yml
                path = ROOT_PATH / "docs"
                docs_generator.render("mkdocs.yml", path=path)

                # append API references to mkdocs.yml
                main_mkdocs()

            case Generate.GenerateOptionsEnum.project:
                assert project_name is not None, "Project name is required for project"
                main_project(project_name)

                Generate.execute(Generate.GenerateOptionsEnum.logo)
                Generate.execute(Generate.GenerateOptionsEnum.licence)

            case Generate.GenerateOptionsEnum.readme:
                Generate.execute(Generate.GenerateOptionsEnum.index_file)
                Generate.execute(Generate.GenerateOptionsEnum.requirements)
                Generate.execute(Generate.GenerateOptionsEnum.installation)
                Generate.execute(Generate.GenerateOptionsEnum.usage)

                path = ROOT_PATH
                docs_generator.concatenate("README.md", path=path)

            case Generate.GenerateOptionsEnum.requirements:
                docs_generator.render("requirements.md")

            case Generate.GenerateOptionsEnum.usage:
                docs_generator.render("usage.md")
