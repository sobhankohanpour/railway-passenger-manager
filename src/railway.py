class Train:
    def __init__(self, last_station, max_cargo_weight, on_trip):
        self.last_station = last_station
        self.max_cargo_weight = max_cargo_weight
        self.on_trip = on_trip


class TrainTrip:
    AVAILABLE_CITIES = (
        'Arak', 'Ardabil', 'Urmia', 'Isfahan', 'Ahvaz', 'Ilam',
        'Bojnord', 'Bandar Abbas', 'Bushehr', 'Birjand', 'Tabriz',
        'Tehran', 'Khorramabad', 'Rasht', 'Zahedan', 'Zanjan', 'Sari',
        'Semnan', 'Sanandaj', 'Shahr-e Kord', 'Shiraz', 'Qazvin', 'Qom',
        'Karaj', 'Kermanshah', 'Gorgan', 'Mashhad', 'Hamadan', 'Yasuj',
        'Yazd'
    )

    def __init__(self, origin_city, destination_city, train):
        self.train = self.validate_train(train)
        self.destination_city = destination_city
        self.origin_city = self.validate_origin_city(origin_city)
        self.passengers = []

    def __call__(self):
        return self.__repr__()

    def validate_origin_city(self, origin_city):
        if origin_city not in TrainTrip.AVAILABLE_CITIES:
            raise Exception("This input is not a verified city!")
        if origin_city == self.destination_city:
            raise Exception("Origin and destination cities can't be the same!")
        if origin_city != self.train.last_station:
            raise Exception(
                "The train for this trip is not available at the origin city!"
            )
        self.origin_city = origin_city
        return self.origin_city

    def validate_train(self, train):
        if not isinstance(train, Train):
            raise Exception("This input is not a train!")
        if train.on_trip:
            raise Exception("This train is currently on another trip!")
        self.train = train
        return self.train

    def __repr__(self):
        remaining_capacity = self.train.max_cargo_weight
        for passenger in self.passengers:
            remaining_capacity -= passenger.cargo_weight
        return remaining_capacity


class Passenger:
    def __init__(self, name, cargo_weight):
        self.name = name
        self.cargo_weight = cargo_weight

    def join_trip(self, trip):
        if self.cargo_weight <= trip():
            trip.passengers.append(self)
        else:
            raise Exception("Heavy load!")

    def leave_trip(self, trip):
        if self in trip.passengers:
            trip.passengers.remove(self)
        else:
            raise Exception("This passenger is not assigned to this trip!")

    def __str__(self):
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