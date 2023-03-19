from read import read_phonebook

def delete_phonebook(line_del):
    phonebook = read_phonebook()
    with open('Phonebook.txt', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    with open('Phonebook.txt', 'w', encoding="utf-8") as f:
        for index, line in enumerate(lines):
            if index != line_del - 1:
                f.write(line)