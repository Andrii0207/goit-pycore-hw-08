from decorator.input_error import input_error
from models.address_book import AddressBook
from models.record import Record


@input_error
def add_contact(args, address_book):

    if len(args) != 2:
        raise ValueError("It must be two arguments")

    name, phone = args

    contact = address_book.find_record(name)

    if contact == None:
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
    else:
        contact.add_phone(phone)

    return "Contact added."
