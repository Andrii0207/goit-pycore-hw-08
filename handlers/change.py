from decorator.input_error import input_error


@input_error
def change_contact(args, address_book):
    name, old_phone, new_phone = args

    record = address_book.find_record(name)

    if not record:
        raise KeyError(f"{name} doesn't exist in contacts")

    if not record.find_phone(old_phone):
        raise ValueError(f"{old_phone} doesn't exist in {name}")

    record.edit_phone(old_phone, new_phone)

    return "Contact updated"
