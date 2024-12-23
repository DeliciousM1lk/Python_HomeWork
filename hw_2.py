class Airplane:
    def __init__(self, airplane_type, max_passengers):
        self.airplane_type = airplane_type
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        return self.airplane_type == other.airplane_type

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, value):
        self.current_passengers += value
        if self.current_passengers > self.max_passengers:
            self.current_passengers = self.max_passengers
        return self

    def __sub__(self, value):
        self.current_passengers -= value
        if self.current_passengers < 0:
            self.current_passengers = 0
        return self

    def __iadd__(self, value):
        return self + value

    def __isub__(self, value):
        return self - value

    def __str__(self):
        return (f"Airplane type: {self.airplane_type}, "
                f"Max passengers: {self.max_passengers}, "
                f"Current passengers: {self.current_passengers}")
if __name__ == '__main__':
    plane1 = Airplane("Boeing 737", 180)
    plane2 = Airplane("Airbus A320", 150)

    print(plane1 == plane2)

    plane1 += 50
    plane2 += 100

    print(plane1)
    print(plane2)

    plane2 -= 30
    print(plane2)

    print(plane1 > plane2)

