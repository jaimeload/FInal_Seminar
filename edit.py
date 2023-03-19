from read import read_phonebook
from name import *

def edit_phonebook(contact_index):

    with open('Phonebook.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        try:
            contact_data = lines[contact_index].strip().split()
            contact_width = [family_width, name_width, patronymic_width, phone_width]
        except IndexError:
            print("Контакт не найден")
            return
        new_data = []
        for i, field in enumerate(["Фамилия", "Имя", "Отчество", "Номер телефона"]):
            value = input(f"Введите новое {field} ({contact_data[i]}): ")
            if value == "":
                new_data.append(contact_data[i].ljust(contact_width[i]))
            else:
                new_data.append(value.ljust(contact_width[i]))

    new_line = "".join(new_data)
    lines[contact_index] = new_line + "\n"
    with open("Phonebook.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)