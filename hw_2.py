class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def set_data(self, title, year, publisher, genre, author, price):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def get_data(self):
        return {
            "Title": self.__title,
            "Year": self.__year,
            "Publisher": self.__publisher,
            "Genre": self.__genre,
            "Author": self.__author,
            "Price": self.__price
        }

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title


if __name__ == "__main__":
    book = Book("1984", 1949, "Secker & Warburg", "Dystopian", "George Orwell", 15.99)
    print(book.get_data())
