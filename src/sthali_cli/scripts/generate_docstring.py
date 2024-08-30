from importlib import import_module
from os import getcwd
from os.path import join as path_join
from jinja2 import Template
from types import ModuleType

from typer import echo

from .commons import to_snake_case, write_file

TEMPLATE = """### `{{ module_name }}`

```
{{ docstring }}
```
"""

def main():
    echo("Generating docs")
    root_path = getcwd()

    echo("Getting project name")
    project_name = root_path.split("/")[-1]
    project_slug = to_snake_case(project_name)

    echo("Getting project module")
    project_module = import_module(project_slug)

    echo("Getting imports from module")
    imports = project_module.__all__
    docs_api_dir = path_join(root_path, "docs/docs/api")
    for i in imports:
        echo(f"Getting docstring from import: {i}")
        attr = getattr(project_module, i)
        docstring = attr.__doc__

        echo("Rendering the template with the data")
        module_name = f"<module {attr.__name__}>" if isinstance(attr, ModuleType) else str(attr)
        doc = Template(TEMPLATE).render(
            module_name=module_name,
            docstring=docstring,
        )

        echo(f"Writing docstring from import: {i}")
        doc_name = to_snake_case(i) if isinstance(attr, ModuleType) else attr.__name__
        doc_path = path_join(docs_api_dir, f"{doc_name}.md")
        write_file(doc_path, doc)
