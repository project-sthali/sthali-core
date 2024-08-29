from os import getcwd
from os.path import join as path_join
from tomli import load
from jinja2 import Template

from typer import echo

from .commons import read_file, write_file

TEMPLATE = """# Requirements

## Prerequisites
- Python {{ python_version }}
- `pip` package manager

## Runtime Dependencies
This project requires the following Python packages with specific versions:
{% for dependency in dependencies %}
- `{{ dependency }}`
{% endfor %}

{% if optional_dependencies %}
## Optional Dependencies
This project has optional dependencies that can be installed for additional features:
{% for group, deps in optional_dependencies.items() %}
### {{ group }}
{% for dep in deps %}
- `{{ dep }}`
{% endfor %}
{% endfor %}
{% endif %}
"""

def main():
    echo("Generating requirements")
    root_path = getcwd()

    echo("Reading pyproject.toml")
    pyproject_dir = path_join(root_path)
    pyproject_path = path_join(pyproject_dir, "pyproject.toml")
    toml_dict = read_file(pyproject_path)

    echo("Getting requirements")
    python_version = toml_dict["project"]["requires-python"]
    dependencies = toml_dict["project"]["dependencies"]
    optional_dependencies = toml_dict["project"]["optional-dependencies"]

    echo("Rendering the template with the data")
    requirements = Template(TEMPLATE).render(
        python_version=python_version,
        dependencies=dependencies,
        optional_dependencies=optional_dependencies
    )

    echo("Writing requirements")
    requirements_dir = path_join(root_path, "docs/docs")
    requirements_path = path_join(requirements_dir, "requirements.md")
    write_file(requirements_path, requirements)
