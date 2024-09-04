from jinja2 import Template
from tomli import loads
from typer import echo

from .commons import PYPROJECT_FILE_PATH, REQUIREMENTS_PATH, File

TEMPLATE = """
---

### Requirements

#### Prerequisites
- `python {{ python_version }}`
- `pip` package manager

#### Runtime Dependencies
This project requires the following Python packages with specific versions:
{% for dependency in dependencies %}
- `{{ dependency }}`
{% endfor %}

{% if optional_dependencies %}
#### Optional Dependencies
This project has optional dependencies that can be installed for additional features:
{% for group, deps in optional_dependencies.items() %}
##### {{ group }}
{% for dep in deps %}
- `{{ dep }}`
{% endfor %}
{% endfor %}
{% endif %}
"""


def main():
    echo("Generating requirements")

    echo("Reading pyproject.toml")
    with File(PYPROJECT_FILE_PATH) as pyproject_file:
        pyproject_file_content = loads(pyproject_file.read())

    echo("Getting requirements")
    python_version = pyproject_file_content["project"]["requires-python"]
    dependencies = pyproject_file_content["project"]["dependencies"]
    optional_dependencies = pyproject_file_content["project"]["optional-dependencies"]

    echo("Rendering the template with the data")
    requirements = Template(TEMPLATE).render(
        python_version=python_version, dependencies=dependencies, optional_dependencies=optional_dependencies
    )

    echo("Writing requirements")
    with File(REQUIREMENTS_PATH, "w") as requirements_file:
        requirements_file.write(requirements)
