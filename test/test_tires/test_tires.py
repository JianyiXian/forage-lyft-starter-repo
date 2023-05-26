import unittest
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [1, 0.3, 0.2, 0.8]

        tires = CarriganTires(
            tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.2, 0.3, 0.2, 0.8]

        tires = CarriganTires(
            tire_wear)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tire_wear = [1, 0.3, 0.2, 3]

        tires = OctoprimeTires(
            tire_wear)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tire_wear = [0.2, 0.3, 0.2, 1]

        tires = OctoprimeTires(
            tire_wear)
        self.assertFalse(tires.needs_service())