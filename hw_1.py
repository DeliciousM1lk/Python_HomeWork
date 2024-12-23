class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.circumference() < other.circumference()

    def __le__(self, other):
        return self.circumference() <= other.circumference()

    def __gt__(self, other):
        return self.circumference() > other.circumference()

    def __ge__(self, other):
        return self.circumference() >= other.circumference()

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __mul__(self, value):
        return Circle(self.radius * value)

    def __truediv__(self, value):
        return Circle(self.radius / value)

    def __str__(self):
        return f"Circle with radius: {self.radius}"

if __name__ == "__main__":
    circle1 = Circle(10)
    circle2 = Circle(15)

    print(circle1 == circle2)
    print(circle1 < circle2)

    circle3 = circle1 + 5
    print(circle3)

    circle1 += 10
    print(circle1)

    circle4 = circle1 * 2
    print(circle4)
