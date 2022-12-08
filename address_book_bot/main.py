from functions.add_data import *
from functions.change_data import *
from functions.delete_data import *
from functions.show_data import *
from db_creation.create_db import create_db

COMMANDS = {
    'add_contact': add_contact,
    'add_phone': add_phone,
    'add_email': add_email,
    'change_phone': change_phone,
    'change_email': change_email,
    'delete_contact': delete_contact,
    'delete_phone': delete_phone,
    'delete_phones': delete_phones,
    'delete_email': delete_email,
    'show_all': show_all,
    'show_contact': show_contact,
    'show_phones': show_phones,
    'show_email': show_email
}


def handler(comm):
    return COMMANDS[comm]


def main():
    connection_string = 'mongodb://localhost:27017'
    db = create_db(connection_string, 'address_book')
    contacts = db['contacts']

    while True:

        user_command = input("Enter a command: ")
        parsed = user_command.split(' ')
        command = parsed[0].lower()

        if command == 'hello':
            print('How can I help you?')

        elif command in ['exit', 'goodbye', 'close']:
            print('Goodbye')
            break

        elif command in COMMANDS.keys():
            print(handler(command)(parsed, contacts))

        else:
            print('No such a command')


if __name__ == 'main':
    main()
