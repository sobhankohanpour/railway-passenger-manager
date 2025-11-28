"""
Railway Passenger & Cargo Management System

This module provides three core classes to simulate a basic railway system:
    - Train:         Represents a physical train and its cargo capacity.
    - TrainTrip:     Defines a trip between two cities, manages passenger assignment,
                     validates trip constraints, and calculates remaining cargo capacity.
    - Passenger:     Represents a traveler with cargo weight and ability to join or leave trips.

The system ensures:
    • A trip can only start if the train is located at the origin city.
    • Origin and destination cities must differ.
    • Passenger cargo weight cannot exceed remaining train capacity.
    • Only trains not already on a trip can be assigned to a new trip.
"""

class Train:
    """Represents a physical train with cargo capacity and travel status.

    This class stores information about a train's last known station,
    its maximum supported cargo capacity, and whether the train is currently
    engaged in a trip. It is primarily used by the `TrainTrip` class to ensure
    that only available trains with sufficient capacity can be assigned
    to new passenger journeys.
    """

    def __init__(self, last_station: str, max_cargo_weight: int | float, on_trip: bool) -> None:
        """Initialize a new Train object.

        :param last_station: Name of the station where the train is currently located.
        :param max_cargo_weight: Maximum cargo weight the train can carry (kg).
        :param on_trip: Indicates whether the train is currently operating on a trip.
        """
        self.last_station = last_station
        self.max_cargo_weight = max_cargo_weight
        self.on_trip = on_trip



class TrainTrip:
    """Represents a scheduled train trip between two cities.

    Validates train availability, origin location, and ensures that
    origin and destination cities are different. Holds passenger objects
    and tracks remaining cargo capacity.

    :raises Exception: If the provided train is invalid or already on a trip.
    :raises Exception: If the origin or destination is not among allowed cities.
    :raises Exception: If the train is located somewhere other than the origin.
    :return: A new TrainTrip instance.
    :rtype: TrainTrip
    """

    AVAILABLE_CITIES = (
        'Arak', 'Ardabil', 'Urmia', 'Isfahan', 'Ahvaz', 'Ilam',
        'Bojnord', 'Bandar Abbas', 'Bushehr', 'Birjand', 'Tabriz',
        'Tehran', 'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 'Sari',
        'Semnan', 'Sanandaj', 'Shahr-e Kord', 'Shiraz', 'Qazvin', 'Qom',
        'Karaj', 'Kermanshah', 'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj',
        'Yazd'
    )

    def __init__(self, origin_city: str, destination_city: str, train: Train) -> None:
        """Initialize trip details and validate constraints.

        :param origin_city: City where the trip begins.
        :param destination_city: City where the trip ends.
        :param train: Train assigned to this route.
        """
        self.train = self.validate_train(train)
        self.destination_city = destination_city
        self.origin_city = self.validate_origin_city(origin_city)
        self.passengers = []

    def __call__(self) -> int | float:
        """Enable using trip() to return remaining cargo capacity.

        :return: Remaining available cargo weight.
        """
        return self.__repr__()

    def validate_origin_city(self, origin_city: str) -> str:
        """Verify that the origin city is valid and matches train location.

        :param origin_city: Starting station of the trip.
        :raises Exception: If city is not listed in AVAILABLE_CITIES.
        :raises Exception: If origin and destination are identical.
        :raises Exception: If train is not physically in the origin city.
        :return: Validated origin city.
        """
        if origin_city not in TrainTrip.AVAILABLE_CITIES:
            raise Exception("This input is not a verified city!")
        if origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")
        if origin_city != self.train.last_station:
            raise Exception("The train for this trip is not available at the origin city!")

        self.origin_city = origin_city
        return self.origin_city

    def validate_train(self, train: Train) -> Train:
        """Validate assigned train before starting the trip.

        :param train: Train object being linked to the trip.
        :raises Exception: If input is not an instance of `Train`.
        :raises Exception: If train is currently busy on another trip.
        :return: Validated train.
        """
        if not isinstance(train, Train):
            raise Exception("This input is not a train!")
        if train.on_trip:
            raise Exception("This train is currently on another trip!")

        self.train = train
        return self.train

    def __repr__(self) -> int | float:
        """Return remaining cargo capacity after loading passengers.

        Iterates through current passenger list and subtracts total cargo 
        weight from max capacity.

        :return: Remaining cargo capacity (kg).
        """
        remaining_capacity = self.train.max_cargo_weight
        for passenger in self.passengers:
            remaining_capacity -= passenger.cargo_weight
        return remaining_capacity



class Passenger:
    """Represents a traveler with assigned cargo weight."""

    def __init__(self, name: str, cargo_weight: int | float) -> None:
        """Store passenger identity and cargo mass.

        :param name: Passenger full name.
        :param cargo_weight: Cargo weight assigned to passenger (kg).
        """
        self.name = name
        self.cargo_weight = cargo_weight

    def join_trip(self, trip: TrainTrip):
        """Add passenger to trip if capacity permits.

        :param trip: TrainTrip instance to join.
        :raises Exception: If passenger cargo exceeds available capacity.
        """
        if self.cargo_weight <= trip():
            trip.passengers.append(self)
        else:
            raise Exception("Heavy load!")

    def leave_trip(self, trip: TrainTrip):
        """Remove passenger from a trip if assigned.

        :param trip: TrainTrip instance to leave.
        :raises Exception: If passenger is not currently in that trip.
        """
        if self in trip.passengers:
            trip.passengers.remove(self)
        else:
            raise Exception("This passenger is not assigned to this trip!")

    def __str__(self) -> str:
        """Return formatted passenger name.

        :return: Passenger name as string.
        """
        return f"{self.name}"



# ==============================
# Test Cases 
# ==============================
if __name__ == "__main__":

    # ---- TrainTrip.__call__ capacity test ----
    train = Train(last_station="Sanandaj", max_cargo_weight=34286, on_trip=False)
    p1 = Passenger(name="Ali Saeedi", cargo_weight=616)
    p2 = Passenger(name="Abolfazl Zandi", cargo_weight=349)

    trip = TrainTrip(origin_city="Sanandaj", destination_city="Rasht", train=train)

    assert trip() == 34286, "Initial capacity should match train weight."
    trip.passengers = [p1]
    assert trip() == 34286 - 616, "Capacity did not decrease correctly."
    trip.passengers = [p1, p2]
    assert trip() == 34286 - 616 - 349, "Multiple passenger weight calc incorrect."

    # ---- Passenger.__str__ test ----
    assert str(p1) == "Ali Saeedi", "String output of passenger should return name only."

    print("\n✔ All Tests Passed Successfully!")