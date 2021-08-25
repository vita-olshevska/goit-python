from address_book import AddressBook, Name, Phone, Birthday, Record


def input_error(func):
    def inner(string):
        try:
            return func(string)
        except KeyError:
            if func.__name__ == "show_phone" or func.__name__ == "change_info":
                return "Incorrect name! \n"
            if func.__name__ == "run_command":
                return "Incorrect command word! \n"
        except ValueError:
            if func.__name__ == "run_command":
                return "Something new except wit Value Error! \n"
        except IndexError:
            if func.__name__ == "run_command":
                return "Something new except wit Index Error for run_command ! \n"
            if func.__name__ == "add_info" or func.__name__ == "change_info":
                return "You need to write 'name' and 'phone' separated with space! \n"

    return inner


def get_name_phone(string):
    info_list = string.split()
    if info_list[0] in ["add", "change"]:
        info_list = info_list[1:]
    name = info_list[0].title()
    phone = info_list[1] + " ".join(info_list[2:])
    return name, phone


def get_name(string):
    info_list = string.split()
    if info_list[0] == "phone":
        info_list = info_list[1:]
    name = info_list[0].title()
    return name


@input_error
def work_on(string):
    return "How can I help you?"


@input_error
def work_off(string):
    return ""


@input_error
def add_info(string):
    global phone_book
    name, phone = get_name_phone(string)
    name_field = Name(name)
    phone_field = Phone(phone)
    new_record = Record(name_field)
    new_record.add(phone_field)
    phone_book.add_record(new_record)
    return f"Added: {phone_book[name]}\n"


@input_error
def change_info(string):
    global phone_book
    name, phone = get_name_phone(string)
    if name not in phone_book:
        return f"Can not find record with name {name}."

    name_field = Name(name)
    phone_field = Phone(phone)
    new_record = Record(name_field)
    new_record.add(phone_field)
    phone_book.add_record(new_record)
    return f"For {name} add new phone {phone}\n"


def parse_user_input(string: str) -> (str, str):
    """ Used only for hard commands """
    if string is None or string == "":
        return "", ""

    parts = string.split()
    command = parts[0]
    if command not in HARD_COMMANDS:
        return "", ""

    if len(parts) == 1:
        return command, ""

    arguments = " ".join(parts[1:])
    return command, arguments


@input_error
def show(string: str):
    _, arguments = parse_user_input(string)
    if arguments == "":
        return show_all_info(arguments)
    elif arguments.isnumeric():
        return "\n".join(["Selected Phone Book information:"] + [f"{val}" for key, val in phone_book.items() if
                                                          any([arguments in phone.value for phone in val.phone_list])])
    elif arguments.isascii():
        return "\n".join(["Selected Phone Book information:"] + [f"{val}" for key, val in phone_book.items() if arguments in key.lower()])
    else:
        return "Unexpected input format!!!"


@input_error
def show_all_info(string):
    return "\n".join(["All information from Phone Book:"] + [f"{val}" for key, val in phone_book.items()])


HARD_COMMANDS = {
    "add": add_info,
    "change": change_info,
    "phone": show,
    "show": show
}

COMMANDS = {
    "hello": work_on,
    "good bye": work_off,
    "close": work_off,
    "exit": work_off,
    "show all": show_all_info
}


@input_error
def run_command(command):
    if command in COMMANDS.keys():
        return COMMANDS[command](command)
    return HARD_COMMANDS[command.split()[0]](command)


if __name__ == "__main__":
    phone_book = AddressBook()
    while True:
        new_command = input(": ").lower()
        response = run_command(new_command)
        if not response:
            print("Good bye!")
            phone_book.dump_data()
            break
        print(response)
