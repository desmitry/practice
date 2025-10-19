class Vehicle:
    """Represents a generic vehicle."""

    def get_description(self):
        """Returns a description of the vehicle."""
        return "This is a generic vehicle."


class Car(Vehicle):
    """Represents a car."""

    def get_description(self):
        """Returns a description of the car."""
        return "This is a car, it has four wheels."


class Bicycle(Vehicle):
    """Represents a bicycle."""

    def get_description(self):
        """Returns a description of the bicycle."""
        return "This is a bicycle, it has two wheels."


class Boat(Vehicle):
    """Represents a boat."""

    def get_description(self):
        """Returns a description of the boat."""
        return "This is a boat, it floats on water."


def demonstrate_descriptions():
    """Demonstrates calling the method for each vehicle."""
    vehicles = [Vehicle(), Car(), Bicycle(), Boat()]
    for vehicle in vehicles:
        print(vehicle.get_description())


demonstrate_descriptions()
