from decorator.input_error import input_error


@input_error
def show_all(_, address_book):

    if not len(address_book.keys()):
        return print("Oops, contacts is empty")

    return address_book.show_all()
