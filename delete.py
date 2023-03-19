from read import read_phonebook

def delete_phonebook(search_term):
    phonebook = read_phonebook()
    with open('Phonebook.txt', 'w', encoding="utf-8") as f:
        for line in phonebook:
            if search_term not in line:
                f.write(line)