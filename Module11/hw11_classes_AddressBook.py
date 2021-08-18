from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self):
        self.__value = None


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.value = name  # name

    @property
    def value(self):
        return self._Field__value

    @value.setter
    def value(self, input_name):
        if type(input_name) is str:
            self._Field__value = input_name
        else:
            print("Wrong type of the name!!!")


class Phone(Field):
    def __init__(self, phone: str = None):
        super().__init__()
        self.value = phone

    @property
    def value(self):
        return self._Field__value

    @value.setter
    def value(self, input_string):
        standard_phone = input_string.remove(" ")\
                       .remove("-").remove("+")\
                       .remove("(").remove(")").removeprefix("38")
        if len(standard_phone) == 10:
            self._Field__value = standard_phone
        else:
            print("Incorrect telephone number!!!")


class Birthday(Field):
    def __init__(self, birthday: str = None):
        super().__init__()
        self.value = birthday
#       self.__value = datetime(year=year, month=month, day=day)

    @property
    def value(self):
        return self._Field__value

    @value.setter
    def value(self, input_string):
        count_separator = input_string.count("-")
        if count_separator != 2:
            print("Incorrect birth data. You need separate with '-': yyyy-mm-dd ")

        year, month, day = [int(x) for x in input_string.split("-")]
        input_data = datetime(year=year, month=month, day=day)
        if input_data and input_data.date() <= datetime.now().date():
            self._Field__value = input_data
        else:
            print("Incorrect birthday data or you wrote a future date!!! You need: yyyy-mm-dd ")


class Record:
    def __init__(self, name: Name, birthday: Birthday = None):
        self.name = name
        self.phone_list = []
        self.birthday = birthday

    def add(self, phone):
        if phone not in self.phone_list:
            self.phone_list.append(phone)

    def delete(self, phone):
        if phone in self.phone_list:
            self.phone_list.remove(phone)

    def change(self, old_phone, new_phone):
        if old_phone in self.phone_list:
            index = self.phone_list.index(old_phone)
            self.phone_list[index] = new_phone

    def days_to_birthday(self):
        if not self.birthday:
            return None

        current_datetime = datetime.now()
        next_birth = datetime(year=current_datetime.year,
                              month=self.birthday.value.month,
                              day=self.birthday.value.day)
        difference = next_birth.date() - current_datetime.date()
        days_to_birth = difference.days
        if days_to_birth < 0:
            next_birth = datetime(year=current_datetime.year+1, month=self.birthday.value.month, day=self.birthday.value.day)
            difference = next_birth.date() - current_datetime.date()
            days_to_birth = difference.days

        return days_to_birth


class AddressBookIterator:
    def __init__(self, address_book: dict, count: int = 1):
        self.__address_book = address_book
        self.__key_list = list(self.__address_book.keys())
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.__address_book):
            raise StopIteration

        right_point = min(self.index + self.count, len(self.__address_book))
        short_dict = {key: self.__address_book[key] for key in self.__key_list[self.index:right_point]}
        self.index += self.count
        return short_dict


class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = record.name.value
        if key not in self.data.keys():
            self.data[key] = record

    def iterator(self, count):
        return AddressBookIterator(self.data, count)
