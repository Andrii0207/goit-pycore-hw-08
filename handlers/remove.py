from decorator.input_error import input_error
from models.record import Record


@input_error
def remove_phone(args, address_book):
    name, deteled_phone = args

    record = address_book.find_record(name)

    if not record:
        raise KeyError(f"{name} doesn't exist in contacts")

    record.remove_phone(deteled_phone)

    return f"Phone number {deteled_phone} has deleted from {name}"
