import unittest

import sthali_core.utils.enum_clients


class TestClients(unittest.TestCase):
    def setUp(self) -> None:
        self.path = sthali_core.utils.enum_clients.pathlib.Path(__file__).parent

    def test_clients_init(self) -> None:
        clients = sthali_core.utils.enum_clients.Clients(self.path)

        self.assertIsInstance(clients, sthali_core.utils.enum_clients.Clients)

    def test_clients_map_is_dict(self) -> None:
        clients = sthali_core.utils.enum_clients.Clients(self.path)

        self.assertIsInstance(clients.clients_map, dict)
