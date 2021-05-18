class Bus:
    """
    A class that describes a Bus.
    """

    num_bus_created = 0  # Variable to keep track on buses created

    def __init__(self, num_off_seats, color, driver):
        self.num_off_seats = num_off_seats
        self.color = color
        self.driver = driver
        self.increment_bus_created()

    def increment_bus_created(self):
        Bus.num_bus_created = self.num_bus_created + 1

    def change_color(self, color):
        self.color = color
