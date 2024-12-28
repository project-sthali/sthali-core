import enum
import importlib
import pathlib
import types


class Config:
    def __init__(self, package_path: str | None, clients_directory: pathlib.Path) -> None:
        self._package_path = package_path or ""
        self._clients_directory = clients_directory

    @property
    def _clients_files(self) -> list[pathlib.Path]:
        clients_path = pathlib.Path(self._package_path) / self._clients_directory
        return list(filter(lambda file: file.stem != "__init__", clients_path.glob("*.py")))

    @property
    def clients_map(self) -> dict[str, types.ModuleType]:
        return {
            file.stem: importlib.import_module(f".{self._clients_directory}.{file.stem}".replace("/", "."), package=self._package_path)
            for file in self._clients_files
        }

    @property
    def ClientEnum(self) -> type[enum.Enum]:
        client_enum_map = {key: key for key in self.clients_map}
        return enum.Enum("ClientEnum", client_enum_map)
