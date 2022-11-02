from abc import ABC, abstractclassmethod


class Vehicle(ABC):
    speed = {
        'car': 30,
        'bike': 50,
        'cng': 15
    }

    def __init__(self, vehicle_type, license_plate, rate, driver) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.driver = driver
        self.speed = Vehicle.speed[vehicle_type]
        self.status = "available"

    @abstractclassmethod
    def start_driving(self):
        pass

    @abstractclassmethod
    def trip_finished(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "started")

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "finished")


class Bike(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "started")

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "finished")


class CNG(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate, driver,) -> None:
        super().__init__(vehicle_type, license_plate, rate, driver)

    def start_driving(self):
        self.status = "unavailable"
        print(self.vehicle_type, self.license_plate, "started")

    def trip_finished(self):
        self.status = "available"
        print(self.vehicle_type, self.license_plate, "finished")
