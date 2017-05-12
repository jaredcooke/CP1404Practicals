from prac8.silveServiceTaxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Hummer", 200, 4)
print(taxi)
taxi.drive(100)
print(taxi.get_fare())
print(taxi)
taxi2 = SilverServiceTaxi("Prius", 100, 2)
print(taxi2)
taxi2.drive(100)
print(taxi2.get_fare())
print(taxi2)