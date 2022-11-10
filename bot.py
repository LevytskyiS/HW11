from contact_book import AddressBook, Record
from datetime import date

'''
    Additional info to some commands:
        'addnum': command + name + new number
        'change' : command + name + existing number + new number
        'delnum' : command + name + existaing number

'''

def decor(func):
    def wrapper(arg):
        try:
            return func(arg)
        except IndexError:
            return 'There is no phone number. Enter name and phone.' # If user didn`t put the number, only name.
        except ValueError: 
            return 'Number must contain only numbers/the number is too short/the date is incorrect.' # If number contains letters
        except KeyError:
            return 'Wrong command. Try again.' # This command is not in the dictionary with commands. 
        except AttributeError:
            return f'You hasn`t set the b-day for this guy yet.'

    return wrapper

@decor 
def greeting(*_):
    return 'How can I help you? '

@decor
def exit_func(*_):
    return 'Good bye!'

@decor
def contact_book(*_):
    return address_book.show_all_contacts()

@decor
def new_contact(list_name_number : list):
    record = Record(list_name_number[0].capitalize())
    record.add_new_phone(int(list_name_number[1]))
    return address_book.add_record(record)

@decor
def add_new_phone_to_contact(list_number_to_add):
    record = address_book[list_number_to_add[0].capitalize()]
    return record.add_new_phone(int(list_number_to_add[1]))
    

@decor
def change_contact(list_available_name_and_new_number: list):
    record = address_book[list_available_name_and_new_number[0].capitalize()]
    return record.change_phone(int(list_available_name_and_new_number[1]), int(list_available_name_and_new_number[2]))
    
@decor 
def phone_number(name_in_book: list):
    record = address_book[name_in_book[0].capitalize()]
    return address_book.search_by_name(record)

@decor
def del_num_from_contact(number_to_be_deleted: list):
    record = address_book[number_to_be_deleted[0].capitalize()]
    return record.delete_phone(int(number_to_be_deleted[1]))

@decor
def set_up_birthday(name_date: list):
    record = address_book[name_date[0].capitalize()]
    return record.set_birthday(date(year=int(name_date[1]), month=int(name_date[2]), day=int(name_date[3])))

@decor
def change_bday(name_newdate: list):
    record = address_book[name_newdate[0].capitalize()]
    return record.change_birthday(date(year=int(name_newdate[1]), month=int(name_newdate[2]), day=int(name_newdate[3])))

@decor
def days_to_bday(name: list):
    record = address_book[name[0].capitalize()]
    return record.days_to_birthday()

FUNCTIONS = {
    'hello' : greeting, 
    'add' : new_contact,
    'addnum': add_new_phone_to_contact,
    'change' : change_contact,
    'phone' : phone_number, 
    'delnum' : del_num_from_contact,
    'show all' : contact_book,
    'setbday' : set_up_birthday,
    'correctbday' : change_bday,
    'daysleft' : days_to_bday,
    'good bye' : exit_func,
    'exit' : exit_func,
    'close' : exit_func,
}

address_book = AddressBook()

@decor
def handle(inp_by_user : str):

    inp_by_user = inp_by_user.lower().split()
    if ' '.join(inp_by_user[0:2]) == 'show all' or ' '.join(inp_by_user[0:2]) == 'good bye':
        func = ' '.join(inp_by_user[0:2])
    else:
        func = inp_by_user[0]
    args = inp_by_user[1:]
    
    if len(inp_by_user) == 1:
        return FUNCTIONS[func](args)

    elif func == 'show all' or func == 'good bye':
        return FUNCTIONS[func](args)

    elif len(inp_by_user) == 2 or len(inp_by_user) > 2:
        return FUNCTIONS[func](args)

while True:
    
    user_input = input('Enter the command: ')
    user_handler = handle(user_input)
    
    if user_handler == 'Good bye!':
        print(user_handler)
        exit()
    elif user_handler:
        print(user_handler)
