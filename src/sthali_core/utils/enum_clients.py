"""{...}."""

import enum
import importlib
import pathlib
import types


class Clients:
    def __init__(self, parent_path: pathlib.Path, package: str | None = None) -> None:
        self.clients_directory = parent_path / pathlib.Path("clients")
        self.package = package or parent_path.name

    @property
    def _clients_file_path(self) -> list[pathlib.Path]:
        return list(filter(lambda file: file.stem != "__init__", self.clients_directory.glob("*.py")))

    @property
    def _src_path(self) -> pathlib.Path:
        return next(filter(lambda x: x.name == "src", self.clients_directory.parents))

    @property
    def clients_map(self) -> dict[str, types.ModuleType]:
        return {
            file_path.stem: importlib.import_module(self._relative_to_formatted(file_path), package=self.package)
            for file_path in self._clients_file_path
        }

    @property
    def enum(self) -> type[enum.Enum]:
        client_enum_map = {key: key for key in self.clients_map}
        return enum.Enum("ClientEnum", client_enum_map)

    def _relative_to_formatted(self, path: pathlib.Path) -> str:
        """Return the relative path to the clients directory."""
        return str(path.relative_to(self._src_path)).strip(".py").replace("/", ".")
