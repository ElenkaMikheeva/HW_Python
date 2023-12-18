def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'


def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact)
        print('\nКонтакт записан!\n')


def read_files():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    return contacts_list


def print_contacts(contacts_list):
    for nn, contact in enumerate(contacts_list, 1):
        print(f'{nn}. {contact}\n')


def copy_contact():
    contacts_list = read_files()
    print_contacts(read_files())
    num_contact = int(input("Введите номер контакта для копирования: "))
    with open('newphonebook.txt', 'a', encoding='utf-8') as file:
        file.write(f'{contacts_list[num_contact - 1]}\n\n')
        print("\n Контакт скопирован! \n")


def search_contact(field=""):
    print(
            "Возможные варианты поиска:\n"
            "1. По фамилии\n"
            "2. По имени\n"
            "3. По отчеству\n"
            "4. По номеру\n"
            "5. По городу\n"
        )
    index_var = int(input("Введите вариант поиска: ")) -1
    search = input("Введите данные для поиска: ")
    with open("phonebook.txt", "r", encoding="utf-8") as file:
        contacts_str = file.read()
    contacs_list = contacts_str.rstrip().split('\n\n')
    for contact_str in contacs_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')


def interface():
    with open("phonebook.txt", "a"):
        pass
    user_input = None
    while user_input != "5":
        print(
            "Возможные варианты действия:\n"
            "1. Добавить контакт\n"
            "2. Вывод списка контактов\n"
            "3. Поиск контакта\n"
            "4. Копировать контакт\n"
            "5. Выход из программы\n"
        )
        user_input = input("Введите вариант: ")
        while user_input not in ("1", "2", "3", "4", "5"):
            print("Некорректный ввод.")
            user_input = input("Введите вариант: ")
        print()
        if user_input == "1": write_contact()
        if user_input == "2": print_contacts(read_files())
        if user_input == "3": search_contact()
        if user_input == "4": copy_contact()

        print()

if __name__ == "__main__":
    interface()
