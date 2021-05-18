import unittest

from main import Bus


class TestBusClass(unittest.TestCase):
    """
    Testcase class for Bus
    """
    def setUp(self) -> None:
        self.bus = Bus(25, "Yellow", "Coach")

    def test_init_method(self):
        self.assertEqual(self.bus.color, "Blue", "Color should be Blue")
        self.assertEqual(self.bus.driver, "Coach", "The driver should be Coach")
        self.assertEqual(self.bus.num_off_seats, 25, "The number of seats should be 25")

    def test_change_color(self):
        self.bus.change_color("Yellow")
        self.assertEqual(self.bus.color, "Yellow", "The should be Yellow.")

    def test_number_of_bus_created(self):
        self.assertEqual(self.bus.num_bus_created, 10, "10 busses should have been created.")
