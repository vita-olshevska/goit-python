from collections import UserDict
from datetime import datetime

import json

DATA = "data.json"


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
    def value(self, input_string: str):
        standard_phone = input_string.replace(" ", "")\
                       .replace("-", "").replace("+", "")\
                       .replace("(", "").replace(")", "").removeprefix("38")
        if len(standard_phone) == 10:
            self._Field__value = standard_phone
        else:
            raise ValueError("Incorrect telephone number!!!")


class Birthday(Field):
    def __init__(self, birthday: str = None):
        super().__init__()
        self.value = birthday

    @property
    def value(self):
        return self._Field__value

    @value.setter
    def value(self, input_string):
        count_separator = input_string.count("-")
        if count_separator != 2:
            raise ValueError("Incorrect birth data. You need separate with '-': yyyy-mm-dd ")

        year, month, day = [int(x) for x in input_string.split("-")]
        input_data = datetime(year=year, month=month, day=day)
        if input_data and input_data.date() <= datetime.now().date():
            self._Field__value = input_data
        else:
            raise ValueError("Incorrect birthday data or you wrote a future date!!! You need: yyyy-mm-dd ")


class Record:
    def __init__(self, name: Name, birthday: Birthday = None):
        self.name = name
        self.phone_list = []
        self.birthday = birthday

    def __str__(self):
        phone_output = ", ".join(phone.value for phone in self.phone_list)
        output = f"{self.name.value} {phone_output}"
        if self.birthday is not None:
            output += self.birthday.value

        return output

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
    def __init__(self):
        super().__init__()
        self.load_data()

    def add_record(self, record: Record):
        key = record.name.value
        if key not in self.data.keys():
            self.data[key] = record
        else:
            for phone in record.phone_list:
                self.data[key].add(phone)

    def iterator(self, count):
        return AddressBookIterator(self.data, count)

    def dump_data(self):
        data = dict()
        for record in self.data.values():
            name = record.name.value
            phone_list = [phone.value for phone in record.phone_list]
            birthday = None
            if record.birthday is not None:
                birthday = record.birthday.value.strftime("%Y:%m:%d")

            data[name] = {"name": name, "phone_list": phone_list, "birthday": birthday}

        with open(DATA, "w") as file:
            json.dump(data, file)

    def load_data(self):
        try:
            with open(DATA) as file:
                data = json.load(file)
        except:
            print("No data available.")
            return

        for data_record in data.values():
            name = Name(data_record["name"])
            birthday = None
            if data_record["birthday"] is not None:
                birthday = Birthday(data_record["birthday"])

            record = Record(name, birthday)
            for phone in data_record["phone_list"]:
                record.add(Phone(phone))

            self.data[data_record["name"]] = record
