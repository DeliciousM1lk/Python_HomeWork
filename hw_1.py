class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def set_data(self, model, year, manufacturer, engine_volume, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def get_data(self):
        return {
            "Model": self.__model,
            "Year": self.__year,
            "Manufacturer": self.__manufacturer,
            "Engine Volume": self.__engine_volume,
            "Color": self.__color,
            "Price": self.__price
        }

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year


if __name__ == "__main__":
    car = Car()
    car.set_data("Model S", 2020, "Tesla", 3.0, "Red", 75000)
    print(car.get_data())
