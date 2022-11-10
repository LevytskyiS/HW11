from collections import UserDict
from datetime import date

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record
        return f'New contact was added successfuly.'

    def search_by_name(self, record):
        if len(record.list_of_obj_of_phone) >= 1:
            return [num.value for num in record.list_of_obj_of_phone]
        else: 
            return f'This guy doesn`t have a number.'
        
    def show_all_contacts(self):
        res = []
        for key, value in self.data.items():
            res.append(key)
            res.append([num.value for num in value.list_of_obj_of_phone])
            if value.birthday:
                res.append(value.birthday.object_date.strftime("%A %d %B %Y"))
            else:
                res.append(value.birthday)
        return res

class Iterable:

    def __init__(self, add_book, number_of_pages):
        self.current_page = 1
        self.add_book = add_book
        self.number_of_pages = number_of_pages
        self.result_pages = []
        
    def __next__(self):
        if self.current_page <= self.number_of_pages:
            for k, v in self.add_book.items():
                print(k, v)
                if v.birthday:
                    result = ' '.join(f'Name: {k} Phone: {v.value} Birthday: {v.birthday.object_date.strftime("%A %d %B %Y")}')
                    self.result_pages.append(result)
                    self.current_page += 1
                    return result
                elif not v.birthday:
                    result = ' '.join(f'Name: {k} Phone: {v.value} Birthday: {v.birthday}')
                    self.result_pages.append(result)
                    self.current_page += 1
                    return result
        raise StopIteration

class IterAddBook:
    def __init__(self, add_book, number_of_pages):
        self.add_book = add_book
        self.number_of_pages = number_of_pages
    
    def __iter__(self):
        return Iterable(self.add_book, self.number_of_pages)


class Field:
    def __init__(self, value) -> None:
        self.value = value

class Name(Field):

    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self): 
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

class Phone(Field):

    def __init__(self, value) -> None:
        self.__value = None
        self.value = value
        super().__init__(value)

    @property
    def value(self): 
        return self.__value

    @value.setter
    def value(self, value):
        if value < 100:
            raise ValueError
        self.__value = value


class Birthday:

    def __init__(self, object_date) -> None:
        self.__object_date = None
        self.object_date = object_date

    @property
    def object_date(self): 
        return self.__object_date

    @object_date.setter
    def object_date(self, object_date):
        if isinstance(object_date, date):
            self.__object_date = object_date


class Record:

    def __init__(self, name) -> None:
        self.name = Name(name)
        self.list_of_obj_of_phone = []
        self.birthday = None
            
    def add_new_phone(self, phone):
        self.list_of_obj_of_phone.append(Phone(phone))
        return f'The phone was added.'
        
    def change_phone(self, phone, new_phone):
        for values in self.list_of_obj_of_phone:
            if values.value == phone:
                values.value = new_phone
                return f'The number was changed.'
            else:
                return f'The number {phone} isn`t in your book.'

    def delete_phone(self, number):
        for values in self.list_of_obj_of_phone:
            if values.value == number:
                self.list_of_obj_of_phone.remove(values)
                return f'The number was deleted successfully.'
            else:
                return f'The number {number} isn`t in your book.'
    
    def set_birthday(self, birthday):
        self.birthday =  Birthday(birthday)
        return f'The birthday was set successfully.'

    def change_birthday(self, new_birthday):
        self.birthday = Birthday(new_birthday)
        return f'The birthday was changed successfully.'
    
    def days_to_birthday(self):
        days_to_bday = self.birthday.object_date - date.today()
        if days_to_bday.days > 0:
            return f'{days_to_bday.days} days to {self.name.value}`s birthday are left. '\
                    f'It will be on {self.birthday.object_date.strftime("%A %d %B %Y")}.'
        else:
            return f'{self.name.value} has already had a birthday. It was on {self.birthday.object_date.strftime("%A %d %B %Y")}.'