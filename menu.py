from read import read_phonebook
from search import search_phonebook
# from edit import edit_phonebook
# from delete import delete_phonebook
# from add import add_phonebook
# from save import save_phonebook

def print_all():
    phonebook = read_phonebook()
    for line in phonebook:
        print(line)

def search():
    search_term = input("Введите строку для поиска: ")
    results = search_phonebook(search_term)
    for line in results:
        print(line)

# def edit():
#     search_term = input("Введите строку для поиска: ")
#     new_data = input("Введите новые данные: ")
#     edit_phonebook(search_term, new_data)

# def delete():
#     search_term = input("Введите строку для поиска: ")
#     delete_phonebook(search_term)

# def add():
#     new_data = input("Введите новые данные: ")
#     add_phonebook(new_data)

# def save():
#     phonebook = read_phonebook()
#     save_phonebook(phonebook)
