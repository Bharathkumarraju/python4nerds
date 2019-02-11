cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_dirven = drivers
carpool_capacity = cars_dirven * space_in_a_car
average_passengers_per_car = passengers / cars_dirven
print("\n"*3)
print("There are", cars, "cars available")
print("----------------------------------")
print("There are only", drivers, "drivers available")
print("----------------------------------")
print("There will be", cars_not_driven, "empty cars today")
print("----------------------------------")
print("We have", passengers, "to car pool today")
print("----------------------------------")
print("we can transport", carpool_capacity, "people today")
print("----------------------------------")
print("We need to put about", average_passengers_per_car, "in each car")
print("----------------------------------")

