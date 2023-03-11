class Point():
    def __init__(self, x_val, y_val):
        self.x = x_val
        self.y = y_val

    def print(self):
        print(f"X value = {self.x}\n"
              f"Y value = {self.y}")

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
        else:
            raise Exception("Too much passengers, can`t take more!")

    def print(self):
        for i, passenger in enumerate(self.passengers):
            print(f"{i+1} passenger - {passenger}")

flight = Flight(3)
for i in range(3):
    flight.add_passenger("Passee")

flight.print()
flight.add_passenger("Me")
print("\n\n")
flight.print()

