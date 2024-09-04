from importlib import import_module
from types import ModuleType

from jinja2 import Template
from typer import echo

from .commons import API_REFERENCE_PATH, PROJECT_SLUG, File, to_snake_case

TEMPLATE = """### `{{ module_name }}`

```
{{ docstring }}
```
"""

def main():
    echo("Generating docs")

    echo("Getting project module")
    project_module = import_module(PROJECT_SLUG)

    echo("Getting imports from module")
    imports = project_module.__all__
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
        doc_path = API_REFERENCE_PATH / f"{doc_name}.md"
        with File(doc_path, "w") as doc_file:
            doc_file.write(doc)
