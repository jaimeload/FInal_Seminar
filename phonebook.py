from os import system
from menu import *

while True:
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