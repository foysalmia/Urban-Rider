import random


class Brta:
    def __init__(self) -> None:
        self.__license = {}

    def driving_test(self, email):
        score = random.randint(0, 100)
        if score >= 33:
            print("Congrats you have Passed")
            license_number = random.randint(5000, 9999)
            self.__license[email] = license_number
            return license_number
        else:
            print("Sorry You have failed")
            return False

    def validate_license(self, email, license):
        for key, value in self.__license.items():
            if key == email and value == license:
                return True
        return False
