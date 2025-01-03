from models.name import Name
from models.phone import Phone
from models.birthday import Birthday


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, deleted_phone):
        idx = next((idx for idx, phone in enumerate(
            self.phones) if phone.value == deleted_phone), None)

        if idx == None:
            raise IndexError("Index not find")
        self.phones.remove(self.phones[idx])

    def edit_phone(self, old_phone, new_phone):
        idx = next((idx for idx, phone in enumerate(
            self.phones) if phone.value == old_phone), None)

        if idx == None:
            raise IndexError("Index not find")
        self.phones[idx] = Phone(new_phone)

    def find_phone(self, searched_phone):
        return next(
            (phone for phone in self.phones if phone.value == searched_phone), None)

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        if self.birthday is None:
            return (f"{self.name.value}'s birthday is doesn't in contacts")
        return (f"{self.name.value}'s birthday is {self.birthday.value}")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
