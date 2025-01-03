from decorator.input_error import input_error


@input_error
def birthdays(address_book):
    return address_book.get_upcoming_birthdays()
