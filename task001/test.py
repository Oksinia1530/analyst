def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')
    
    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            name = get_search_name()
            print(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, phone_book)
        elif choice == 6:
            do_change_description = change_description()
            for index, dictionary in enumerate(phone_book):
                if dictionary.get("Фамилия") == do_change_description:
                    new_description = input("Введите новое описание для абонента: ")
                    phone_book[index]["Описание"]=new_description
                    break
        elif choice ==7:
            do_del_record = del_record()      
            for index, dictionary in enumerate(phone_book):
                if dictionary.get("Фамилия") == do_del_record:
                    phone_book.pop(index)
                    break
                else:
                    print('Такого пользователя нет в справочнике')
            write_txt('phon.txt', phone_book)
            print(do_del_record, phone_book)
        choice = show_menu()
    
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Внести изменения в справочник\n"
          "7. Удалить запись\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')



def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get("Фамилия") == last_name:
            return el.get("Телефон")
    return "Такой абонент отсутвует"


def find_by_number(data: list, phone_number: str) -> str:
    for el in data:
        if el.get("Телефон") == phone_number:
            return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой абонент отсутвует"


def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def get_search_name():                                      
    return input("Введите фамилию: ")

def get_search_number():
    return input("Введите номер телефона: ")


def get_new_user():
    return input("Введите новую запись в словарь: ")


def get_file_name():
    return input("Введите название файла: ")

def change_description():
    return input('Введите Фамилию абонента, у которого меняем описание: ')

def del_record():                        #Удаляем строку
    return input('Введите Фамилию удаляемого абонента: ')

def print_result(phone_book):
    print(phone_book)

work_with_phonebook()