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
    # перевірити чи вже є таке ім'я
    # якщо є, то запитати чи цей телевон перезаписатти або ж добавити додатково
    phone_book[name] = phone
    return f"Added: {name}: {phone_book[name]}\n"


@input_error
def change_info(string):
    global phone_book
    name, phone = get_name_phone(string)
    # перевірити чи вже є таке ім'я
    old_phone = phone_book[name]
    phone_book[name] = phone
    return f"For {name} changed phone {old_phone} to {phone_book[name]}\n"


@input_error
def show_phone(string):
    name = get_name(string)
    # перевірити чи вже є таке ім'я
    return f"{name}: {phone_book[name]} \n"


@input_error
def show_all_info(string):
    return "\n".join(["All information from Phone Book:"] + [f"{key}: {val}" for key, val in phone_book.items()])


HARD_COMMANDS = {
    "add": add_info,
    "change": change_info,
    "phone": show_phone,
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
    phone_book = {}
    while True:
        new_command = input(": ").lower()
        response = run_command(new_command)
        if not response:
            print("Good bye!")
            break
        print(response)
