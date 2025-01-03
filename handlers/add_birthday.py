from decorator.input_error import input_error


@input_error
def add_birthday(args, address_book):

    if len(args) != 2:
        raise ValueError("It must be two arguments")

    name, birthday = args
    contact = address_book.find_record(name)

    if not contact:
        raise KeyError(f"{name} doesn't exist in contacts")

    contact.add_birthday(birthday)

    return "Birthday added."
