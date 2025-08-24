import unittest

import sthali_core.utils.enum_clients


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.path = sthali_core.utils.enum_clients.pathlib.Path(__file__).parent

    def test_config_init(self) -> None:
        config = sthali_core.utils.enum_clients.Config(self.path)

        self.assertIsInstance(config, sthali_core.utils.enum_clients.Config)
