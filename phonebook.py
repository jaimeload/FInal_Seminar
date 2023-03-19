import os
from os import system
from menu import *
from read import read_phonebook

current_directory = os.path.dirname(os.path.abspath('Phonebook.py'))
phonebook_path = os.path.join(current_directory, 'Phonebook.txt')

def create_empty_file(phonebook_path):
    with open(phonebook_path, 'w') as file:
        pass

while True:
    if not os.path.exists(phonebook_path):
        create_empty_file(phonebook_path)
    print("1. Вывести все записи")
    print("2. Поиск записей")
    print("3. Редактирование записей")
    print("4. Удаление записей")
    print("5. Добавление новых записей")
    print("6. Сохранить изменения")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        print_all()
    elif choice == "2":
        search()
    elif choice == "3":
        edit()
    elif choice == "4":
        delete()
    elif choice == "5":
        add()
    elif choice == "6":
        save()
    elif choice == "0":
        break
    else:
        print("Некорректный выбор")