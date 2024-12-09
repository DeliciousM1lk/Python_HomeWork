class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def __str__(self):
        return f"{self.brand} {self.model} (Power: {self.power}W)"


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_tank_volume, has_milk_frother):
        super().__init__(brand, model, power)
        self.water_tank_volume = water_tank_volume
        self.has_milk_frother = has_milk_frother

    def make_coffee(self):
        return "Making a cup of coffee!"

    def __str__(self):
        frother = "with milk frother" if self.has_milk_frother else "without milk frother"
        return f"{super().__str__()}, Water Tank: {self.water_tank_volume}L, {frother}"


class Blender(Device):
    def __init__(self, brand, model, power, blade_material, capacity):
        super().__init__(brand, model, power)
        self.blade_material = blade_material
        self.capacity = capacity

    def blend(self):
        return "Blending ingredients!"

    def __str__(self):
        return f"{super().__str__()}, Blade Material: {self.blade_material}, Capacity: {self.capacity}L"


class MeatGrinder(Device):
    def __init__(self, brand, model, power, mincing_speed, has_reverse):
        super().__init__(brand, model, power)
        self.mincing_speed = mincing_speed
        self.has_reverse = has_reverse

    def grind_meat(self):
        return "Grinding meat!"

    def __str__(self):
        reverse = "with reverse function" if self.has_reverse else "without reverse function"
        return f"{super().__str__()}, Mincing Speed: {self.mincing_speed}kg/h, {reverse}"


if __name__ == "__main__":
    coffee_machine = CoffeeMachine("DeLonghi", "ECAM22.110", 1450, 1.8, True)
    blender = Blender("Philips", "HR3573/90", 1000, "Stainless Steel", 2.2)
    meat_grinder = MeatGrinder("Bosch", "MFW68660", 2200, 4.3, True)

    print(coffee_machine)
    print(coffee_machine.make_coffee())

    print(blender)
    print(blender.blend())

    print(meat_grinder)
    print(meat_grinder.grind_meat())
