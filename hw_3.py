class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def set_data(self, name, opening_date, country, city, capacity):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def get_data(self):
        return {
            "Name": self.__name,
            "Opening Date": self.__opening_date,
            "Country": self.__country,
            "City": self.__city,
            "Capacity": self.__capacity
        }

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    stadium = Stadium("Camp Nou", "1957-09-24", "Spain", "Barcelona", 99354)
    print(stadium.get_data())
