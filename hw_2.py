class Wheels:
    def __init__(self, wheel_count, wheel_type):
        self.wheel_count = wheel_count
        self.wheel_type = wheel_type

    def __str__(self):
        return f"{self.wheel_count} {self.wheel_type} wheels"


class Engine:
    def __init__(self, engine_type, horsepower):
        self.engine_type = engine_type
        self.horsepower = horsepower

    def start_engine(self):
        return "Engine started!"

    def __str__(self):
        return f"{self.engine_type} engine with {self.horsepower} horsepower"


class Doors:
    def __init__(self, door_count, door_type):
        self.door_count = door_count
        self.door_type = door_type

    def open_doors(self):
        return "Doors opened!"

    def __str__(self):
        return f"{self.door_count} {self.door_type} doors"


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, model, wheel_count, wheel_type, engine_type, horsepower, door_count, door_type):
        Wheels.__init__(self, wheel_count, wheel_type)
        Engine.__init__(self, engine_type, horsepower)
        Doors.__init__(self, door_count, door_type)
        self.brand = brand
        self.model = model

    def start_car(self):
        return f"{self.brand} {self.model} is starting... {self.start_engine()}"

    def __str__(self):
        return f"{self.brand} {self.model}, {self}."


if __name__ == "__main__":
    car = Car("Toyota", "Camry", 4, "all-season", "V6", 301, 4, "manual")
    
    print(car)
    print(car.start_car())
    print(car.open_doors())
