from read import read_phonebook


def edit_phonebook(contact_index):
    # family_width = 15
    # name_width = 15
    # patronymic_width = 15
    # phone_width = 12

    with open('Phonebook.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        try:
            contact_data = lines[contact_index].strip().split()
            contact_width = [15, 15, 15, 12]
        except IndexError:
            print("Контакт не найден")
            return
        new_data = []
        for i, field in enumerate(["Фамилия", "Имя", "Отчество", "Номер телефона"]):
            value = input(f"Введите новое {field} ({contact_data[i]}): ")
            new_data.append(value or contact_data[i].ljust(contact_width[i] - 2))

    new_line = "  ".join(new_data)
    lines[contact_index] = new_line + "\n"
    with open("Phonebook.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)