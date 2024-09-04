from enum import Enum


class Command(str, Enum):
    api_reference = "api-reference"
    # docs = "docs"
    docstring = "docstring"
    project = "project"
    readme = "readme"
    requirements = "requirements"


class Generate:
    def __init__(self, command: Command, project_name: str | None = None):
        self.command = command
        self.project_name = project_name

    def execute(self):
        if self.command == Command.api_reference:
            from .generate_api_reference import main

            main()
        # if self.command == Command.docs:
            # pass
        if self.command == Command.docstring:
            from .generate_docstring import main

            main()
        if self.command == Command.project:
            from .generate_project import main

            main(self.project_name)
        if self.command == Command.readme:
            from .generate_readme import main

            main()
        if self.command == Command.requirements:
            from .generate_requirements import main

            main()
