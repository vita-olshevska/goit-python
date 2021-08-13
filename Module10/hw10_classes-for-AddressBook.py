from collections import UserDict


class Field:
    def __init__(self):
        self.value = None


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.value = name  # name


class Phone(Field):
    def __init__(self):
        super().__init__()
        self.value = ""   # phone


class Record:
    def __init__(self, name: Name):
        self.name = name
        self.phone_list = []

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


class AddressBook(UserDict):
    def add_record(self, record: Record):
        key = record.name.value
        if key not in self.data.keys():
            self.data[key] = record
