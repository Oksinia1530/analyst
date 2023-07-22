# Необходимо написать проект, содержащий функционал работы с заметками. 
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

def work_with_notebook():
    choice = show_menu()
    note_book = read_txt('note.txt')
    
    while (choice != 8):
        if choice == 1:
            print_result(note_book)
        elif choice == 2:
            name = get_search_name()
            print(find_note_date(note_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_note_header(note_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(note_book, user_data)
            write_txt('note.txt', note_book)
        elif choice == 5:
            file_name = get_file_name()
            write_txt(file_name, note_book)
        elif choice == 6:
            do_change_description = change_description()
            for index, dictionary in enumerate(note_book):
                if dictionary.get("ID") == do_change_description:
                    new_description = input("Введите новую заметку: ")
                    note_book[index]["Заметка"]=new_description
                    break
        elif choice ==7:
            do_del_record = del_record()      
            for index, dictionary in enumerate(note_book):
                if dictionary.get("ID") == do_del_record:
                    note_book.pop(index)
                    break
                else:
                    print('Такой заметки нет')
            write_txt('note.txt', note_book)
            print(do_del_record, note_book)
        choice = show_menu()
    
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить всю книжку заметок\n"
          "2. Найти заметку по ID\n"
          "3. Найти заметку по Заголовку\n"
          "4. Добавить Заметку\n"
          "5. Сохранить книжку заметок в текстовом формате\n"
          "6. Внести изменения в заметку\n"
          "7. Удалить заметку\n"
          "8. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename: str) -> list:
    data = []
    fields = ["ID", "Дата", "Заголовок", "Заметка"]
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



def find_note_date(data: list, last_date: str) -> str:
    for el in data:
        if el.get("ID") == last_date:
            return el.get("Заметка")
    return "Такой заметки нет"


def find_note_header(data: list, note_header: str) -> str:
    for el in data:
        if el.get("Заголовок") == note_header:
            return f'{el.get("Дата")}, {el.get("Заметка")}'
    return "Такая заметка отсутствует"


def add_user(data: list, user_data: str):
    fields = ["ID", "Дата", "Заголовок", "Заметка"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def get_search_name():                                      
    return input("Введите ID Заметки: ")

def get_search_number():
    return input("Введите Заголовок заметки: ")


def get_new_user():
    return input("Введите новую заметку: ")


def get_file_name():
    return input("Введите название файла: ")

def change_description():
    return input('Введите ID изменяемой заметки: ')

def del_record():                        #Удаляем строку
    return input('Введите ID удаляемой заметки: ')

def print_result(note_book):
    for line in note_book:
        print(line)

work_with_notebook()