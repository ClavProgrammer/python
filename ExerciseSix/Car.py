class Car:

    def __init__(self, registration_mark, car_type, driven_km):
        self.registration_mark = registration_mark
        self.car_type = car_type
        self.driven_km = driven_km
        self.is_lend = True

    def lend_car(self):
        if self.is_lend:
            self.is_lend = not self.is_lend
            return ("Confirm that car was lend.")
        else:
            return("Car is not available.")

    def get_info(self):
        return (f"registration mark: {self.registration_mark}, car type: {self.car_type}, driven km: {self.driven_km}")