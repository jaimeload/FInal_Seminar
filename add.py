def add_phonebook(new_data):
    with open('Phonebook.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(new_data)