from parser import parse_input
from handlers import add, all_contacts, change, remove, show, delete, remove, add_birthday, show_birthday, birthdays
from models.address_book import AddressBook
from models.record import Record


def main():
    contacts_book = AddressBook()

    record1_init = Record("John")
    record1_init.add_phone("1234567890")
    record1_init.add_phone("5555555555")
    record1_init.add_phone("1122334455")
    record1_init.add_birthday("04.01.2002")
    contacts_book.add_record(record1_init)

    record2_init = Record("Jane")
    record2_init.add_phone("9876543210")
    record2_init.add_birthday("23.04.1994")
    contacts_book.add_record(record2_init)

    record3_init = Record("Sarah")
    record3_init.add_phone("0987654321")
    record3_init.add_birthday("05.01.2020")
    contacts_book.add_record(record3_init)

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add.add_contact(args, contacts_book))

        elif command == "change":
            print(change.change_contact(args, contacts_book))

        elif command == "phone":
            print(show.show_phone(args, contacts_book))

        elif command == "all":
            print(all_contacts.show_all(args, contacts_book))

        elif command == "delete":
            print(delete.delete_contact(args, contacts_book))

        elif command == "remove":
            print(remove.remove_phone(args, contacts_book))

        elif command == "add-birthday":
            print(add_birthday.add_birthday(args, contacts_book))

        elif command == "show-birthday":
            print(show_birthday.show_birthday(args, contacts_book))

        elif command == "birthdays":
            print(birthdays.birthdays(contacts_book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
