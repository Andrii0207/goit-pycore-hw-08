from collections import UserDict
from datetime import datetime, timedelta


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record(self, name):
        if name in self.data:
            return self.data[name]

    def show_all(self):
        contact_list = []

        for name, record in self.data.items():
            contact = dict()
            contact[name] = [phone.value for phone in record.phones]
            contact_list.append(contact)
        return contact_list

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def remove_phone(self, deleted_phone):
        print("remove_phone: ", deleted_phone)
        # next(
        #     (phone for phone in self.phones if phone.value == deleted_phone), None)

    def get_upcoming_birthdays(self):

        congratulation_list = []
        current_date = datetime.today().date()

        for _, record in self.data.items():
            birthday = record.birthday

            if birthday == None:
                continue

            date = birthday.value

            comparing_year = current_date.year

            if (date.month, date.day) < (current_date.month, current_date.day):
                comparing_year = current_date.year + 1

            comparing_date = datetime(
                comparing_year, date.month, date.day).date()

            if comparing_date < current_date or comparing_date >= current_date + timedelta(days=7):
                continue

            congrats_date = comparing_date

            if comparing_date.weekday() == 5:
                congrats_date = comparing_date + timedelta(days=2)
            elif comparing_date.weekday() == 6:
                congrats_date = comparing_date + timedelta(days=1)

            congratulation_list.append(
                {"name": record.name.value, "birthday_date": str(date), 'congratulation_date': congrats_date.strftime("%d.%m.%Y")})

        return sorted(congratulation_list, key=lambda elem: elem["congratulation_date"])
