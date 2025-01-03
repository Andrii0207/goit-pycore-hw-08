from decorator.input_error import input_error


@input_error
def show_phone(args, address_book):
    name = args[0]

    record = address_book.find_record(name)

    if not record:
        raise KeyError(f"{name} doesn't exist in contacts")

    return record
