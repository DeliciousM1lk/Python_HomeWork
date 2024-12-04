class MainClass:
    def __init__(self, text=""):
        self.__text = text

    def set_text(self, text=""):
        self.__text = text

    def get_text(self):
        return self.__text


class DerivedClass(MainClass):
    def __init__(self, text="", number=0):
        super().__init__(text)
        self.__number = number

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number


if __name__ == "__main__":
    main_obj = MainClass("Hello")
    print(main_obj.get_text())

    derived_obj = DerivedClass("Derived Text", 42)
    print(derived_obj.get_text(), derived_obj.get_number())
