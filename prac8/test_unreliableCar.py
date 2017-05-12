from prac8.unreliableCar import UnreliableCar

unreliableCar_test = UnreliableCar('some old car', 100, 60)
unreliableCar_test.drive(40)
print(unreliableCar_test)
unreliableCar_test.add_fuel(40)
print(unreliableCar_test)
unreliableCar_test.drive(140)
print(unreliableCar_test)