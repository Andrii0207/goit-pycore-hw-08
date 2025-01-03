from decorator.error_paint import error_paint


def input_error(func):
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except KeyError as error:
            return error_paint(error, "KeyError")
        except ValueError as error:
            return error_paint(error, "Give me name and phone please.")
        except IndexError as error:
            return error_paint(error, "Please add a contact name")

    return inner
