# Справочник
# 1. Показывать все контакты
# 2. Создавать новый контакт
# 3. Поиск по контактам
# 4. Изменение контакта
# 5. Удаление контакта
# Контакт должен содержать имя и фамилию, номер телефона и комментарий

def start_menu(file, operation):
    dictionary = {'1': show_all_directory,
                  '2': add_new_contact,
                  '3': change_contact,
                  '4': delete_contact,
                  '5': find_in_contacts,
                  '6': import_contact,
                  '0': finish}
    try:
        dictionary[operation](file)
    except KeyError:
        print("\nСледует выбирать действие из ПРЕДЛОЖЕННЫХ вариантов !!!\n")


def add_new_contact(file):
    name = input("Введите имя и фамилию >>> ")
    phone = input("Введите номер телефона >>> ")
    comment = input("Введите комментарий о контакте >>> ")
    with open(file, 'a', encoding='utf8') as data:
        data.write(f'{name} \t {phone} \t {comment}\n')


def read_file(file) -> str:
    directory_str = ''
    try:
        with open(file, 'r', encoding='utf8') as data:
            for line in data:
                directory_str += line
        if len(directory_str) == 0:
            print('\nСправочник пуст!!! Добавьте свой первый контакт в справочник,\nвыбрав пункт меню '
                  '"Создать новый контакт".\n')
        return directory_str
    except FileNotFoundError:
        print('\nФайл-справочник не найден!\n')


def show_all_directory(file):
    print(read_file(file))


def change_contact(file):
    directory_str = read_file(file)
    if directory_str == None or directory_str == '':
        return
    directory_list = directory_str.split('\n')
    print(directory_str)
    choice_person = input("Введите часть строки являющейся уникальной для изменяемого контакта >>> ")
    if choice_person in directory_str:  # проверяем, есть ли в справочнике контакт, который юзер хочет изменить
        current_contact = ''
        line_numb = 0
        for i in range(len(directory_list) - 1):
            if bool(directory_list[i].count(choice_person)):
                line_numb = i
                current_contact = directory_list.pop(i)
        current_contact_list = current_contact.split(' \t ')
        choice_action = input('1 - редактировать имя и фамилию \n2 - редактировать тел. номер \n3 - редактировать '
                              'комментарий \nВыберите желаемое действие со справочником >>> ')
        match choice_action:
            case '1':
                new_contact_data = input("Введите новое имя и фамилию >>> ")
                current_contact_list[0] = new_contact_data
            case '2':
                new_contact_data = input("Введите новый телефонный номер >>> ")
                current_contact_list[1] = new_contact_data
            case '3':
                new_contact_data = input("Введите новый комментарий >>> ")
                current_contact_list[2] = new_contact_data
            case _:
                print("\nВыберите данные для редактирования из ПРЕДЛОЖЕННЫХ вариантов !!!")
        new_contact = ' \t '.join(current_contact_list)
        directory_list.insert(line_numb, new_contact)
        with open(file, 'w', encoding='utf8') as data:
            for i in range(len(directory_list) - 1):
                data.write(f'{directory_list[i]}\n')
    else:
        print('Контакт с введенными данными в справочнике не найден.')


def delete_contact(file):
    directory_str = read_file(file)
    if directory_str == None or directory_str == '':
        return
    directory_list = directory_str.split('\n')
    print(directory_str)
    user_choice = input("Введите часть строки являющейся уникальной для удаляемого контакта >>> ")
    if user_choice in directory_str:  # проверяем, есть ли в справочнике контакт, который юзер хочет удалить
        for pers in directory_list:
            if bool(pers.count(user_choice)):
                print(f'\nЗапись справочника "{pers}" успешно удалена!\n')
                directory_list.remove(pers)
        with open(file, 'w', encoding='utf8') as data:
            for i in range(len(directory_list) - 1):
                data.write(f'{directory_list[i]}\n')
    else:
        print('Контакт с введенными данными в справочнике не найден.')


def find_in_contacts(file):
    directory_str = read_file(file)
    if directory_str == None or directory_str == '':
        return
    user_looking_for = input("Введите известные данные о контакте >>> ")
    if user_looking_for in directory_str:
        directory_list = directory_str.split('\n')
        for pers in directory_list:
            if bool(pers.count(user_looking_for)):
                print(pers)
    else:
        print("Поиск по справочнику не дал результата.")


def import_contact(file):
    file_source = input("Введите имя файла-справочника, из которого хотите импортировать контакт"
                        " в формате *****.txt >>> ")
    directory_str = read_file(file_source)
    if directory_str == None or directory_str == '':
        return
    directory_list = directory_str.split('\n')
    directory_tuple = tuple(enumerate(directory_list))
    for contact in directory_tuple:
        print(f'{int(contact[0]) + 1} - {contact[1]}')
    number_of_contact = input("Введите порядковый номер импортируемого контакта >>> ")
    contact = directory_list[int(number_of_contact) - 1]
    with open(file, 'a', encoding='utf8') as data:
        data.write(f'{contact}\n')
        print(f"Контакт импортирован в файл-справочник {file}!")


def finish(file):
    pass


if __name__ == '__main__':
    my_contacts = 'file.txt'
    action = ''
    while action != '0':
        action = input('1 - Показать все контакты \n2 - Создать новый контакт \n3 - Изменить контакт '
                       '\n4 - Удалить контакт \n5 - Поиск по контактам \n6 - Импорт контакта \n0 - Выход '
                       '\nВыберите желаемое действие со справочником >>> ')
        start_menu(my_contacts, action)
    print("\nСпасибо за использование нашего справочника!")
