import importlib
import pathlib
import types
import typing

import jinja2
import pydantic
import typer

from ..commons import API_REFERENCE_PATH, PROJECT_SLUG, File, to_snake_case

TEMPLATE = """{{ heading_level * '#' }} `{{ name }}`

```
{{ docstring }}
```

{% if sub %}{{ sub }}{% endif %}
"""


def get_metadata(obj: typing.Any) -> str | None:
    metadata: list[typing.Any] = getattr(obj, "__metadata__", [])
    field_info = next(filter(lambda x: isinstance(x, pydantic.fields.FieldInfo), metadata), None)
    if field_info:
        return field_info.description
    return None


def get_doc(obj: typing.Any) -> str | None:
    return getattr(obj, "__doc__", None)


def get_docstring(obj: typing.Any) -> str:
    metadata = get_metadata(obj)
    doc = get_doc(obj)
    return metadata or doc or ""


def render(name: str, docstring: str, level: int = 3, sub: str | None = None) -> str:
    return jinja2.Template(TEMPLATE).render(
        name=name,
        docstring=docstring,
        heading_level=level,
        sub=sub,
    )


@pydantic.dataclasses.dataclass
class Doc:
    name: str
    path: pathlib.Path
    docstring: str
    level: int
    sub: list["Doc"]


def recursive_writer(doc: Doc) -> str:
    typer.echo(f"Writing docstring from import: {doc.name}")

    to_render = render(doc.name, doc.docstring, doc.level, "\n".join([recursive_writer(s) for s in doc.sub]))
    with File(doc.path, "w") as doc_file:
        doc_file.write(to_render)

    return to_render


TypesMapping = typing.Literal["module", "function", "class"]


def get_import_type_mapping(_import: typing.Any) -> TypesMapping | None:
    import_type: typing.Any = type(_import)
    match import_type:
        case types.ModuleType:
            return "module"
        case types.FunctionType:
            return "function"
        case _ if isinstance(_import, type):
            return "class"
        case _:
            return None


def get_imports_from_module(module: types.ModuleType, level: int, append: bool = True) -> list[Doc]:
    typer.echo(f"Getting imports from {module.__name__} module")

    docs: list[Doc] = []
    for i in getattr(module, "__all__", []):
        typer.echo(f"Getting metadata from {i} import")

        _import = getattr(module, i)
        name = _import.__name__
        filename = _import.__name__
        sub = []
        import_type = get_import_type_mapping(_import) or ""
        if import_type == "module":
            name = _import.__spec__.name
            sub = get_imports_from_module(_import, level + 1)
            filename = to_snake_case(i)

        docs.append(
            Doc(
                name=name,
                path=API_REFERENCE_PATH / f"{import_type}_{filename}.md",
                docstring=get_docstring(_import),
                level=level,
                sub=sub,
            ),
        )
    return docs


def main():
    typer.echo(f"Generating docs for {PROJECT_SLUG}")

    project_module = importlib.import_module(PROJECT_SLUG)
    heading_level = 3
    imports_from_module = get_imports_from_module(project_module, heading_level)

    typer.echo("Clearing API Reference folder")
    for doc in API_REFERENCE_PATH.glob("*"):
        doc.unlink()

    for doc in imports_from_module:
        recursive_writer(doc)
