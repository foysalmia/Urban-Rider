import hashlib
import random

from BRTA import Brta
from ridemanager import uber
from vehicle import CNG, Bike, Car

license_authority = Brta()


class User:
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        pass_enc = hashlib.md5(password.encode()).hexdigest()
        with open("user.txt", "w") as file:
            file.write(f"{email} {pass_enc}")
        file.close()

    @staticmethod
    def log_in(email, password):
        with open("user.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                db_email, db_pass = line.split(" ")
        file.close()
        password = hashlib.md5(password.encode()).hexdigest()
        if email == db_email and password == db_pass:
            print("User Logged in Successfully")
        else:
            print("User not Logged in.")


class Rider(User):
    def __init__(self, name, email, password, locataion, balance) -> None:
        self.location = locataion
        self.balance = balance
        super().__init__(name, email, password)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def request_trip(self, destination):
        pass

    def start_a_trip(self, fare):
        self.balance -= fare


class Driver(User):
    def __init__(self, name, email, password, location, license) -> None:
        self.location = location
        self.license = license
        self.valid_driver = license_authority.validate_license(email, license)
        self.earning = 0
        super().__init__(name, email, password)

    def start_a_trip(self, destionation, fare):
        self.earning += fare
        self.location = destionation

    def take_driving_test(self):
        result = license_authority.driving_test(self.email)
        if result == False:
            self.license = None
        else:
            self.license = result
            self.valid_driver = True

    def register_a_vehicle(self, vehicle_type, license_plate, rate):
        if self.valid_driver:
            if vehicle_type == 'car':
                new_vehicle = Car(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            elif vehicle_type == "bike":
                new_vehicle = Bike(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)
            else:
                new_vehicle = CNG(
                    vehicle_type, license_plate, rate, self)
                uber.add_a_vehicle(vehicle_type, new_vehicle)

        else:
            pass


# creating users
user1 = Rider("Foysal", "mfoysal314@gmail.com",
              "123456", random.randint(0, 30), 1000)
user2 = Rider("user2", "user2@gmail.com", "user2",
              random.randint(0, 30), 5645)
user3 = Rider("user3", "user3@gmail.com", "user3",
              random.randint(0, 30), 5645)

# creating drivers
for i in range(1, 100):
    driver1 = Driver(f"driver{i}", f"driver{i}@mail.com",
                     f"driver{i}", random.randint(0, 100), random.randint(1000, 9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle("car", random.randint(10000, 99999), 10)


print(uber.get_available_cars())
print("\n")
uber.find_a_vehicle(user1, 'car', random.randint(1, 100))
uber.find_a_vehicle(user1, 'car', random.randint(1, 100))
uber.find_a_vehicle(user1, 'car', random.randint(1, 100))
uber.find_a_vehicle(user1, 'car', random.randint(1, 100))
uber.find_a_vehicle(user1, 'car', random.randint(1, 100))
