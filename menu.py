from read import read_phonebook
from search import search_phonebook
from edit import edit_phonebook
from delete import delete_phonebook
from add import add_phonebook
from save import save_phonebook

def print_all():
    print('\n')
    phonebook = read_phonebook()
    for line in phonebook:
        print(line)
    print('\n')

def search():
    search_term = input("Введите строку для поиска: ")
    results = search_phonebook(search_term)
    print('\n')
    for line in results:
        print(line)
    print('\n')

def edit():
    contact_index = int(input("Введите номер записи, которую нужно отредактировать: ")) - 1
    print(contact_index)
    edit_phonebook(contact_index)

def delete():
    search_term = input("Введите строку для поиска: ")
    delete_phonebook(search_term)

def add():
    family = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    add_phonebook(family, name, patronymic, phone)

def save():
    phonebook = read_phonebook()
    save_phonebook(phonebook)