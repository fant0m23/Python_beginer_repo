# Справочник
# 1. Показывать все контакты
# 2. Создавать новый контакт
# 3. Поиск по контактам
# 4. Изменение контакта
# 5. Удаление контакта
# Контакт должен содержать имя и фамилию, номер телефона и комментарий

def main():
    dictionary = {'1': show_all_directory,
                  '2': add_new_contact,
                  '3': change_contact,
                  '4': delete_contact,
                  '5': find_in_contacts,
                  '6': finish}
    operation = input('1 - Показать все контакты \n2 - Создать новый контакт \n3 - Изменить контакт '
                      '\n4 - Удалить контакт \n5 - Поиск по контактам \n6 - Выход \nВыберите желаемое '
                      'действие со справочником >>> ')
    try:
        dictionary[operation]()
    except KeyError:
        print("\nВыберете действие из ПРЕДЛОЖЕННЫХ вариантов !!!")
        main()


def add_new_contact():
    name = input("Введите имя и фамилию >>> ")
    phone = input("Введите номер телефона >>> ")
    comment = input("Введите комментарий о контакте >>> ")
    with open('file.txt', 'a', encoding='utf8') as data:
        data.write(f'{name} \t {phone} \t {comment}\n')
    main()


def read_file() -> str:
    directory_str = ''
    try:
        with open('file.txt', 'r', encoding='utf8') as data:
            for line in data:
                directory_str += line
        return directory_str
    except FileNotFoundError:
        print('\nСправочник пуст!!! Добавьте свой первый контакт в справочник.\n')
        add_new_contact()


def show_all_directory():
    print(read_file())
    main()


def change_contact():
    directory_str = read_file()
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
                print("\nВыберете данные для редактирования из ПРЕДЛОЖЕННЫХ вариантов !!!")
                change_contact()
        new_contact = ' \t '.join(current_contact_list)
        directory_list.insert(line_numb, new_contact)
        with open('file.txt', 'w', encoding='utf8') as data:
            for i in range(len(directory_list) - 1):
                data.write(f'{directory_list[i]}\n')
        main()
    else:
        print('Контакт с введенными данными в справочнике не найден.')
        main()


def delete_contact():
    directory_str = read_file()
    directory_list = directory_str.split('\n')
    print(directory_str)
    user_choice = input("Введите часть строки являющейся уникальной для удаляемого контакта >>> ")
    for pers in directory_list:
        if bool(pers.count(user_choice)):
            print(f'\nЗапись справочника "{pers}" успешно удалена!\n')
            directory_list.remove(pers)
    with open('file.txt', 'w', encoding='utf8') as data:
        for i in range(len(directory_list) - 1):
            data.write(f'{directory_list[i]}\n')
    main()


def find_in_contacts():
    directory_str = read_file()
    user_looking_for = input("Введите известные данные о контакте >>> ")
    if user_looking_for in directory_str:
        directory_list = directory_str.split('\n')
        for pers in directory_list:
            if bool(pers.count(user_looking_for)):
                print(pers)
    else:
        print("Поиск по справочнику не дал результата.")
    main()


def finish():
    print("\nСпасибо за использование нашего справочника!")


if __name__ == '__main__':
    main()
