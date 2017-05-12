from prac7.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        chance_fail = randint(0, 100)
        if chance_fail < self.reliability:
            super().drive(distance)
