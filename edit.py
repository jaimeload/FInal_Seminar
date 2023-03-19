from read import read_phonebook

def edit_phonebook(search_term, new_data):
    phonebook = read_phonebook()
    with open('Phonebook.txt', 'w', encoding="utf-8") as f:
        for line in phonebook:
            if search_term in line:
                f.write(new_data + '\n')
            else:
                f.write(line)