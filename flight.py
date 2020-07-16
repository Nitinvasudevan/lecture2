class Flight ():
    def __init__(self,capcity):
        self.capacity = capcity
        self.passangers = []

    def add_passangers (self,name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

people = ["A", "B", "C", "D"]

for i in people:
    if flight.add_passangers(i):
        print(f"Was able to add person {i}")
    else:
        print(f"Was not able to add person {i}. All Full")