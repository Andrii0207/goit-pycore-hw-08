from models.field import Field
from datetime import datetime


class Birthday(Field):
    def __init__(self, value):

        try:
            if type(value) != str:
                raise TypeError()

            datetime_birthday = datetime.strptime(value, "%d.%m.%Y").date()

            super().__init__(datetime_birthday)

        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


datetime_birthday = datetime.strptime("10.10.2000", "%d.%m.%Y")
