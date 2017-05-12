from prac8.taxi import Taxi

class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return "{} plus flagfall of $4.50".format(super().__str__())

    def get_fare(self):
        return super().get_fare() + 4.5
