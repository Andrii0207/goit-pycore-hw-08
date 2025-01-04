import pickle
from models.address_book import AddressBook


class Database:
    def __init__(self, filename="addressbook.pkl"):
        self.__filename = filename

    def save_data(self, contacts_book=AddressBook):
        with open(self.__filename, "wb") as file:
            pickle.dump(contacts_book, file)

    def load_data(self):
        try:
            with open(self.__filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return AddressBook()
