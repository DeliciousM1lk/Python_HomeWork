class BaseClass:
    def __init__(self, text=""):
        self.__text = text

    def set_text(self, text=None):
        if text is None:
            self.__text = "Default Text"
        else:
            self.__text = text

    def get_text(self):
        return self.__text

    def __str__(self):
        return f"Text: {self.__text}"


class DerivedClass(BaseClass):
    def __init__(self, text="", number=0):
        super().__init__(text)
        self.__number = number

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def __str__(self):
        base_text = super().__str__()
        return f"{base_text}, Number: {self.__number}"


if __name__ == "__main__":
    base_obj = BaseClass("Hello, World!")
    print(base_obj)

    base_obj.set_text()
    print(base_obj)

    derived_obj = DerivedClass("Hello, Derived!", 42)
    print(derived_obj)

    derived_obj.set_text("Updated Text")
    derived_obj.set_number(100)
    print(derived_obj)
