import time

from car import Car


class CarManager:
    def __init__(self,car_number):
        self.cars = []
        self.time = time.time()
        self.car_number = car_number
        self.cars.append(Car())

    def move_cars(self,distance):
        for car in self.cars:
            car.forward(distance)
        self.check_for_wallhit()
        self.add_new_car()

    def add_new_car(self):
        if len(self.cars)<self.car_number and (time.time() - self.time > 0.01):
            self.cars.append(Car())
            self.time = time.time()

    def check_for_wall_hit(self):
        for car in self.cars:
            car.check_for_wall_hit()