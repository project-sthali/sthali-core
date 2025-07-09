import unittest

import sthali_core.utils.base


class TestConfig(unittest.TestCase):
    def test_return_default(self) -> None:
        result = sthali_core.utils.base.Config("")

        self.assertIsInstance(result, sthali_core.utils.base.Config)


class TestAppSpecification(unittest.TestCase):
    def test_app_specification_return_default(self) -> None:
        result = sthali_core.utils.base.AppSpecification()

        self.assertIsInstance(result, sthali_core.utils.base.AppSpecification)


class TestApp(unittest.TestCase):
    def test_app_return_default(self) -> None:
        app_specification = sthali_core.utils.base.AppSpecification()

        result = sthali_core.utils.base.App(app_specification)

        self.assertIsInstance(result, sthali_core.utils.base.App)
