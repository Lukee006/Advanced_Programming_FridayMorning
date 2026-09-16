from rental import Vehicle, Renter, ElectricCar, Motorbike


car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV123", 75)
motorbike = Motorbike("Honda", "CB500", "BK123", 500)

renter = Renter("John", 12345)

print(car)

car.rent()
print(car)

car.return_vehicle()
print(car)


try:
    bad_renter = Renter("", 12345)
except ValueError as e:
    print("Error:", e)


try:
    bad_renter = Renter("Alice", -5)
except ValueError as e:
    print("Error:", e)


vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)